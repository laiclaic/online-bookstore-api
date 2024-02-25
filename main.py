# api endpoints

from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from models import *
from utils import *

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books

@app.get("/book/{code}")
def get_book(code: str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.code == code).first()
    if book is None:
        raise HTTPException(status_code=404, detail="not found")
    return book

@app.post("/book/create")
def create_book(title: str, author: str, classification: str, publisher: str, desc: str, price: float, db: Session = Depends(get_db)):
    # create new book in the database
    obj_book = Book(
        code=code_generator(title),
        title=title,
        author=author,
        classification=classification,
        publisher=publisher,
        desc=desc,
        price=price
    )
    db.add(obj_book)
    db.commit()
    db.refresh(obj_book)
    return obj_book