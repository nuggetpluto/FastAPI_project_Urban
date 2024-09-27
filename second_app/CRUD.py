from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app_2 = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app_2.get("/users")
def get_users():
    return users



@app_2.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    # Находим максимальный ключ и добавляем нового пользователя с ключом +1
    new_key = str(max([int(k) for k in users.keys()]) + 1)
    users[new_key] = f"Имя: {username}, возраст: {age}"
    return f"User {new_key} is registered"


@app_2.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app_2.delete("/user/{user_id}")
def delete_user(user_id: str):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    else:
        raise HTTPException(status_code=404, detail="User not found")
