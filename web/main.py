from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return{"Hello":"World"}

@app.get("/item/{item_id}")
def show_item(item_id:int):
    return {"item id":item_id}

@app.get("/class/")
def show_class(class_id:int, class_name:str):
    return{"class id":class_id, "class name":class_name}