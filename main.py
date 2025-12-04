from fastapi import FastAPI

api = FastAPI()

# GET, POST, PUT, DELETE

@api.get('/')
def index():
    return { "message": "Hello World" }

# uvicorn main:api --port 9999