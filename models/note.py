from typing import Optional
from pydantic import BaseModel


class Note(BaseModel):
    title: str
    des:str
    importance: Optional[bool] = None