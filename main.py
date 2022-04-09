from fastapi import FastAPI

app=FastAPI()


@app.get("/{id}")
def index(id:int):
    return {"name":id}