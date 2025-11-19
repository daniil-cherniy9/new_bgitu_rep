from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
from models import Movie

app = FastAPI()
templates = Jinja2Templates(directory="templates")

os.makedirs("static/uploads", exist_ok=True)

movie1 = Movie(name='The Shawshank Redemption', id=1, cost=25000000, director='Frank Darabont')
movie2 = Movie(name='The Godfather', id=2, cost=6000000, director='Francis Ford Coppola')
movie3 = Movie(name='The Dark Knight', id=3, cost=185000000, director='Christopher Nolan')
movie4 = Movie(name='Pulp Fiction', id=4, cost=8000000, director='Quentin Tarantino')
movie5 = Movie(name='Forrest Gump', id=5, cost=55000000, director='Robert Zemeckis')
movie6 = Movie(name='Inception', id=6, cost=160000000, director='Christopher Nolan')
movie7 = Movie(name='The Matrix', id=7, cost=63000000, director='Lana Wachowski')
movie8 = Movie(name='Goodfellas', id=8, cost=25000000, director='Martin Scorsese')
movie9 = Movie(name='The Silence of the Lambs', id=9, cost=19000000, director='Jonathan Demme')
movie10 = Movie(name='Saving Private Ryan', id=10, cost=70000000, director='Steven Spielberg')

movies_list = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10]


@app.get("/add_movie", response_class=HTMLResponse)
async def add_new_movie(request: Request):
    return templates.TemplateResponse("form_add_new_movie.html", {"request": request})


@app.post("/get_movie")
async def add_new_movie_post(
    name: str = Form(...),
    director: str = Form(...),
    cost: int = Form(...),
    rating: int = Form(...)
):
    new_id = len(movies_list) + 1

    new_movie = Movie(
        id=new_id,
        name=name,
        director=director,
        cost=cost,
        rating=rating
    )

    movies_list.append(new_movie)

    return {
        "message": "Movie added successfully",
        "all_movies": [movie.dict() for movie in movies_list]
    }
@app.get("/movie/{movie_id}", response_class=HTMLResponse)
async def movie_detail(request: Request, movie_id: int):
    movie = next((m for m in movies_list if m.id == movie_id), None)
    if not movie:
        return {"error": "Movie not found"}
    return templates.TemplateResponse("movie_detail.html", {"request": request, "movie": movie})


@app.get("/")
async def root():
    return {"message": "Главная страница"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8165)
