from fastapi import FastAPI
from models import Movie
from fastapi.responses import HTMLResponse

app = FastAPI()

# user1 = User(name="John Doe", id=1, age=20)
# user2 = User(name="Doe John", id=2, age=20)
# user3 = User(name="1r2r23r", id=3, age=30)
# list_users = [user1, user2, user3]

movie1 = Movie(name='movie_1', id=1, cost=3000, director='afsefse')
movie2 = Movie(name='movie_2', id=2, cost=3000, director='afsefse')
movie3 = Movie(name='movie_3', id=3, cost=3000, director='afsefse')
movie4 = Movie(name='movie_4', id=4, cost=3000, director='afsefse')
movie5 = Movie(name='movie_5', id=5, cost=3000, director='afsefse')
movie6 = Movie(name='movie_6', id=6, cost=3000, director='afsefse')
movie7 = Movie(name='movie_7', id=7, cost=3000, director='afsefse')
movie8 = Movie(name='movie_8', id=8, cost=3000, director='afsefse')
movie9 = Movie(name='movie_9', id=9, cost=3000, director='afsefse')
movie10 = Movie(name='movie_10', id=10, cost=3000, director='afsefse')

movies_list = [movie1, movie2, movie3,movie4, movie5,movie6,movie7,movie8,movie9,movie10]

@app.get("/")
async def root():
    for movie in movies_list:
        if movie.id==id:
            return movie

@app.get("/study")
async def get_users():
    with open("index.html", 'r', encoding="utf-8") as file_study:
        html_content = file_study.read()
    return HTMLResponse(content=html_content)

@app.get('/movietop/{name}')
async def get_name_movie(name:str):
    for movie in movies_list:
        if movie.name == name:
            return movie

@app.get("/movietop/{id}")
async def get_movie(id: int):
    for movie in movies_list:
        if movie.id == id:
            return movie

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8165)
