from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from auth import create_access_token, get_current_user, users_db
from database import add_movie, get_all_movies

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login_form(
    username: str = Form(...),
    password: str = Form(...)
):
    if username not in users_db or users_db[username] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(username)

    return JSONResponse({
        "access_token": access_token,
        "token_type": "bearer"
    })


@app.get("/add_film", response_class=HTMLResponse)
async def add_film_page(request: Request):
    return templates.TemplateResponse("add_film.html", {"request": request})


@app.post("/get_movie")
async def get_movie_post(
    request: Request,
    name: str = Form(...),
    director: str = Form(...),
    cost: int = Form(...),
    rating: int = Form(...),
    token: str = Form(...)
):
    username = get_current_user(token)

    new_movie = add_movie(name, director, cost, rating)
    return {"message": "Film added successfully", "film": new_movie.model_dump()}

@app.get("/")
async def root():
    return {"message": "Главная страница"}


@app.get("/films")
async def get_films():
    return get_all_movies()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8165)
