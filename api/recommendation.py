
def recommend(user_id, top=10):
    liked_film_id = ratings[(ratings['user_id'] == user_id) & ((ratings['rating'] == 4) | (ratings['rating'] == 5))].sample(1)['movie_id'].values[0]
    sim_films_id = movie_similarity[liked_film_id - 1].argsort()[-1-top:-1] + 1
    print(f'Those films similar to "{movies.loc[movies["movie_id"] == liked_film_id, "title"].values[0]}", film id: {liked_film_id}')
    print('_'*50)
    for i in sim_films_id[::-1]:
        print(movies.loc[movies['movie_id'] == i, 'title'].values[0])