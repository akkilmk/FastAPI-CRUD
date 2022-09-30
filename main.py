from fastapi import FastAPI
import datetime

date = datetime

app = FastAPI(

    title="CRUD Program", description=" Sample Program"

)


@app.get("/")
def root():
    return {"message": "welcome to fast api"}


@app.get("/about/ok")
def about(id=5):
    data = {"data": {"message": {id * 100}}}
    print(type(data))
    return data


@app.get("/about/{id}")
def about(id: int):
    lists= []
    data = {"data": {"message": {id * 100}}}
    for i in range(id):
        lists.append(data)
    return lists