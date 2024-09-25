from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def welcome():
    return "Главная страница!"


@app.get("/user/admin")
async def get_admin_page():
    return "Вы вошли как администратор!"



@app.get("/user/{user_id}")
async def get_user_number(user_id: int):
    return f"Вы вошли как пользователь №{user_id}!"

@app.get("/user")
def read_user_info(username: Optional[str] = None, age: Optional[int] = None):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
