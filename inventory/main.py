from re import U
from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException

from models import Article, ArticleUpdate
#instance 
app = FastAPI()

db: List[Article] = [
    Article(
        id=UUID("59c19943-44cc-4e9d-b769-66ec7544e32f"),
        topic="REST API Introduction",
        author="Ria",
        para="Let's break it into two components: 1) RESTful 2) API An API is an interface through which one program or web site talks to another.They are used to share data and services, and they come in many different formats and types.",
        dateC="2022-09-12"),
    Article(
        id=UUID("773898bd-3911-47fe-9c7a-2176ddb601a0"),
        topic="FastAPI",
        author="Payal",
        para="FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.",
        dateC="2021-05-12")


]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/articles")
async def fetch_articles():
    return db;
 
@app.post("/api/articles")
async def add_article(article:Article):
    db.append(article)
    return {"id": article.id}

@app.put("/api/articles")
async def edit_article(article:Article):
    for i in range(len(db)):
        if db[i].id==article.id:
            db[i]=article
    return db;

@app.put("api/articles/{article_id}")
async def update_article(article_update: ArticleUpdate,article_id:UUID):
    for article in db:
        if article.id==article_id:
            if article_update.topic is not None:
                article.topic=article_update.topic
            if article_update.author is not None:
                article.author=article_update.author
            if article_update.para is not None:
                article.para=article_update.para
            if article_update.dateC is not None:
                article.dateC=article_update.dateC
            return db;
    raise HTTPException(
        status_code=404,
        detail=f"article with id: {article_id} does not exist"
    )

@app.delete("/api/articles/{article_id}")
async def delete_article(article_id:UUID):
    for article in db:
        if article.id==article_id:
            db.remove(article)
            return
    raise HTTPException(
        status_code=404,
        detail=f"article with id : {article_id} does not exist"

    )