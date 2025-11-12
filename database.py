from models import Movie

movies_list = [
    Movie(name='movie_1', id=1, cost=3000, director='director1'),
    Movie(name='movie_2', id=2, cost=3000, director='director2')
]

def add_movie(name: str, director: str, cost: int, rating: int):
    new_id = max(movie.id for movie in movies_list) + 1 if movies_list else 1
    new_movie = Movie(id=new_id, name=name, director=director, cost=cost, rating=rating)
    movies_list.append(new_movie)
    return new_movie

def get_all_movies():
    return movies_list
