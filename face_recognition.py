import cv2
import dlib
import numpy as np


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


shape_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


face_recognition_model = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')


known_face_encodings = []
known_face_names = []


def add_known_face(name, face_image):
    face_locations = face_cascade.detectMultiScale(face_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(face_locations) == 1:
        shape = shape_predictor(face_image, face_locations[0])
        face_encoding = np.array(face_recognition_model.compute_face_descriptor(face_image, shape))
        known_face_names.append(name)
        known_face_encodings.append(face_encoding)
        return True
    return False


add_known_face('Person A', cv2.imread('person_a.jpg'))
add_known_face('Person B', cv2.imread('person_b.jpg'))


cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_image = frame[y:y + h, x:x + w]

        
        shape = shape_predictor(frame, dlib.rectangle(x, y, x + w, y + h))
        face_encoding = np.array(face_recognition_model.compute_face_descriptor(frame, shape))

       
        matches = dlib.fhog_object_detector.run(known_face_encodings, face_encoding)
        
        name = "Unknown"
        if matches:
            name = known_face_names[matches[0]]

       
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == 27: 
        break


cap.release()
cv2.destroyAllWindows()
