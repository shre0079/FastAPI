from fastapi import FastAPI

app=FastAPI()

db: List[User]=[
    User(id=uuid4(),first_name="Shreyash", last_name="Mishra", gender=Gender.male, roles=[Role.student]),
    User(id=uuid4(),first_name="Shreyash", last_name="", gender=Gender.male, roles=[Role.admin, Role.user, Role.student])
]

@app.get("/")
async def root():
    return {"Hello":"Shreyash"}

@app.get("/ping")
async def root():
    return {"pong"} 