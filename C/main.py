from fastapi import FastAPI, HTTPException, Request, Form, Depends, Response
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import uuid
from datetime import datetime, timedelta
from typing import Dict
from models import Movie

app = FastAPI()
templates = Jinja2Templates(directory="templates")

sessions: Dict[str, dict] = {}
users_db = {"admin": "admin", "user": "user"}

movie1 = Movie(name='The Shawshank Redemption', id=1, cost=25000000, director='Frank Darabont', rating=5)
movies_list = [movie1]


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

    sessions[session_token]["expires_at"] = datetime.now() + timedelta(minutes=2) # эта штука продлит сессию на 2 минуты
    return session_data


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login_form(response: Response, username: str = Form(...), password: str = Form(...)):
    if username not in users_db or users_db[username] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

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
        max_age=120
    )

    return {"message": "Login successful"}


@app.get("/user")
async def get_user_profile(current_user: dict = Depends(get_current_user)):
    if not current_user:
        return JSONResponse(
            status_code=401,
            content={"message": "Unauthorized"}
        )

    profile_info = {
        "username": current_user["username"],
        "session_created_at": current_user["created_at"].isoformat(),
        "session_expires_at": current_user["expires_at"].isoformat(),
        "movies": [movie.dict() for movie in movies_list]
    }

    return profile_info


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8165)
