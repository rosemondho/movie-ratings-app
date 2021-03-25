import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')
model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    title = movie['title']
    overview = movie['overview']
    poster_path = movie['poster_path']

    date_str = movie.get('release_date')
    format_str = '%Y-%m-%d'
    new_date = datetime.strptime(date_str, format_str)

    db_movie = crud.create_movie(title, overview, new_date, poster_path)
    movies_in_db.append(db_movie)


for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    new_user = crud.create_user(email,password)

    for r in range(10):
        new_rating = crud.create_rating(new_user,choice(movies_in_db),randint(1,5))
