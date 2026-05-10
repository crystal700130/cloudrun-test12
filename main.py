from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello"}

@app.get("/test")
def test():
    return {"n": 6}
