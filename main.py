from fastapi import FastAPI
from models import User

app = FastAPI()

user1 = User(name="John Doe", id=1, age=20)
user2 = User(name="Doe John", id=2, age=20)
user3 = User(name="1r2r23r", id=3, age=30)
list_users = [user1, user2, user3]

@app.get("/")
async def root():
    return {"message": "Главная страница приложения"}

@app.get("/users")
async def get_users():
    return list_users
    # return list_users[0].name

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
