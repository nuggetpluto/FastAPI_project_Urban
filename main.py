from fastapi import FastAPI,Path
from typing import Optional
from typing import Annotated
app = FastAPI()


@app.get("/")
def get_main_page():
    return "Главная страница!"


@app.get("/user/admin")
def get_admin_page():
    return "Вы вошли как администратор!"



@app.get("/user/{user_id}")
def read_user(user_id: Annotated[int, Path(description="Enter User ID", ge=1, le=100)]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[str, Path(description="Enter username", min_length=5, max_length=20)],
    age: Annotated[int, Path(description="Enter age", ge=18, le=120)]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

