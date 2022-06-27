from datetime import date
from pydoc_data.topics import topics
from turtle import st
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel





class Article(BaseModel):
    id: Optional[UUID]=uuid4()
    topic: str
    author: str
    para: str
    dateC: date

class ArticleUpdate(BaseModel):
    topic: Optional[str]
    author: Optional[str]
    para: Optional[str]
    dateC: Optional[date]

   
