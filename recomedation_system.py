import pandas as pd


data = {
    'User': ['User1', 'User2', 'User3', 'User4', 'User5'],
    'Movie1': [5, 4, 0, 0, 1],
    'Movie2': [4, 5, 2, 0, 0],
    'Movie3': [0, 0, 5, 4, 0],
    'Movie4': [0, 2, 0, 5, 4],
    'Movie5': [1, 0, 0, 0, 5]
}

df = pd.DataFrame(data)


def recommend_movies(user):
   
    user_ratings = df[df['User'] == user]

    
    user_corr = df.corrwith(user_ratings, axis=1, method='pearson')

    
    corr_df = pd.DataFrame(user_corr, columns=['Correlation'])

   
    corr_df = corr_df.sort_values(by='Correlation', ascending=False)

    
    corr_df = corr_df[corr_df.index != user]

    
    recommendations = df.loc[corr_df.index[0]]  

    return recommendations[recommendations > 0].index.tolist()


user = 'User1'
movie_recommendations = recommend_movies(user)
print(f"Recommended movies for {user}: {', '.join(movie_recommendations)}")
