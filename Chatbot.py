import random


rules = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a chatbot, but I'm here to help you!", "I'm doing well, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?", "I'm just a simple chatbot."]
}


def chatbot_response(user_input):
    user_input = user_input.lower()  
    
    
    for key in rules:
        if key in user_input:
            return random.choice(rules[key])
    
    
    return random.choice(rules["default"])


print("Chatbot: Hi! How can I assist you today? (Type 'bye' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
