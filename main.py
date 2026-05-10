from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Cloud Run"}

@app.get(“/test")
def test():
    return {"n": 3+3}
