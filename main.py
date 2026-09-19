from typing import List
from uuid import uuid4

from fastapi import FastAPI

from models import Gender, Role, User

app=FastAPI()

db: List[User]=[
    User(id=uuid4(), first_name="Shreyash", last_name="Mishra", gender=Gender.male, role=Role.student),
    User(id=uuid4(), first_name="Narendra", last_name="Modi", gender=Gender.male, role=Role.admin)
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