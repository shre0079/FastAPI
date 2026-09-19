from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return {"Hello":"Shreyash"}

@app.get("/ping")
async def root():
    return {"pong"} 