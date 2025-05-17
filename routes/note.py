from fastapi import APIRouter, Request

from models.note import Note


from fastapi.responses import HTMLResponse
from config.db import conn
from schemas.note import noteConvertor, noteEntity
from fastapi.templating import Jinja2Templates
templates=Jinja2Templates(directory="templates")

note = APIRouter()
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.note.notes.find()
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id" : doc["_id"],
            "title":doc["title"],
            "des":doc["des"],
            "importance":doc["importance"]
        })
    
    return templates.TemplateResponse("index.html", {"request": request, "newDocs":newDocs})


@note.post("/") 
async def create_item(request: Request):
    form = await request.form()
    # print(form)
    print(form)
    print(form.get("importance"))
    formDict = dict(form)
    
    formDict["importance"] = True if formDict.get("importance") == "on" else False
    print(form.get("importance"))
    note = conn.note.notes.insert_one(formDict)
    
    return{"Sucess": "Note Created", "id": str(note.inserted_id)}

# @app.post("/")
# async def create_item(request: Request):
#     form = await request.form()
#     formDict = dict(form)
    
#     note = conn.note.notes.insert_one(formDict)
#     return {"Success": "Note Created", "id": str(note.inserted_id)}