from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!!"}

@app.get("/version")
def get_version():
    return {"version": "3.0", "message": "This is a new change for testing auto-deployment!"}

