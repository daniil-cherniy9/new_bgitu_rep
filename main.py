from fastapi import FastAPI, HTTPException, Request, Form, Depends, status, Response
from models import Movie
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import uuid
from datetime import datetime, timedelta
from typing import Dict

app = FastAPI()

templates = Jinja2Templates(directory="templates")

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

movies_list = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10]

sessions: Dict[str, dict] = {}
users_db = {
    "admin": "admin",
    "user": "user"
}

@app.get("/")
async def root():
    return {"message": 'Главная страница'}

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

@app.get("/add_movie", response_class=HTMLResponse)
async def add_new_movie(request: Request):
    return templates.TemplateResponse("form_add_new_movie.html", {"request": request})

@app.post("/get_movie")
async def add_new_movie_post(
    name: str = Form(...),
    director: str=Form(...),
    cost: int=Form(...),
    rating: int=Form(...)
):
    new_id = max(movie.id for movie in movies_list) + 1 if movies_list else 1

    new_movie = Movie(
        id=new_id,
        name=name,
        director=director,
        cost=cost,
        rating = rating
    )

    movies_list.append(new_movie)

    return RedirectResponse(url="/all_movies_json", status_code=303)

@app.get("/all_movies_json")
async def show_all_movies_json():
    return movies_list

@app.get("/movietop/{id}")
async def get_movie(id: int):
    for movie in movies_list:
        if movie.id == id:
            return movie

def get_current_user(request: Request):
    session_token = request.cookies.get("session_token")
    if not session_token:
        return None

    session_data = sessions.get(session_token)
    if not session_data:
        return None

    if datetime.now() > session_data["expires_at"]:
        del sessions[session_token]
        return None

    sessions[session_token]["expires_at"] = datetime.now() + timedelta(minutes=2)

    return session_data

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login_form(response: Response, username: str = Form(...), password: str = Form(...)):
    if username not in users_db or users_db[username] != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    session_token = str(uuid.uuid4())
    expires_at = datetime.now() + timedelta(minutes=2)

    sessions[session_token] = {
        "username": username,
        "created_at": datetime.now(),
        "expires_at": expires_at
    }

    response.set_cookie(
        key="session_token",
        value=session_token,
        httponly=True,
        max_age=120,
        secure=False
    )

    return {"message": "Login successful"}

@app.get("/user")
async def get_user_profile(current_user: dict = Depends(get_current_user)):
    if not current_user:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "Unauthorized"}
        )

    profile_info = {
        "username": current_user["username"],
        "session_created_at": current_user["created_at"].isoformat(),
        "session_expires_at": current_user["expires_at"].isoformat(),
        "movies": [movie.dict() for movie in movies_list]
    }

    return profile_info

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8165)
