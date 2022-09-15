from datetime import date
from pydoc_data.topics import topics
from turtle import st
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel





class Article(BaseModel):
    title: str
    abstract: str
    venue: str
    year: str