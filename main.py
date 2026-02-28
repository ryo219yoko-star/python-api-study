from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Yuzuki's house"}

@app.get("/hello")
def hello():
    return {"msg": "hello world"}