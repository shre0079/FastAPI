from typing import List
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException

from models import Gender, Role, User, UserUpdateRequest

app=FastAPI()

db: List[User]=[
    User(id=uuid4(), first_name="Shreyash", last_name="Mishra", gender=Gender.male, role=[Role.student]),
    User(id=uuid4(), first_name="Narendra", last_name="Modi", gender=Gender.male, role=[Role.admin, Role.user])
]

@app.get("/")
async def root():
    return {"Hello":"Shreyash"}

@app.get("/ping")
async def root(): 
    return {"pong"} 

@app.get("/api/v1/users")
async def fetch_users():
    return db;  

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id: ":user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return user_id;
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id==user_id:
            user.first_name=user_update.first_name
            user.last_name=user_update.last_name
            user.middle_name=user_update.middle_name
            user.roles=user_update.roles
            return user_id
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )