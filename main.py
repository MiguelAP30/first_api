from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def greet():
    return "Hello World"

@app.get('/{id}')
def greet(id):
    return f"Hello World {id}"