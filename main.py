
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates=Jinja2Templates(directory="templates")


conn = MongoClient("mongodb+srv://mongo:8273014786@a1.xt108yk.mongodb.net") 

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.note.notes.find()
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id" : doc["_id"],
            "note":doc["note"]
        })
    print(docs)
    return templates.TemplateResponse("index.html", {"request": request, "newDocs":newDocs})




@app.get("/items/{item_id}")
def read_item(item_id: int, q: str| None = None):
    return {"item_id": item_id, "q": q}