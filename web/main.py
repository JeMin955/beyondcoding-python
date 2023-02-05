#dir/cd web/uvicorn main:app --reload
from typing import Union
from urllib import request

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"),name='static')

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.get("/items/{item_id}") # path parameter
def show_item(item_id:int):
    return {"item id":item_id}

@app.get("/class/")
def show_class(class_id:int, class_name:str): #query parameter
    return{"class id":class_id, "class name":class_name}

@app.get("/calculator/")
def calculator(first_num:str, op:str, second_num:str):
    result = eval(first_num + op + second_num)
    return {"result":result}

