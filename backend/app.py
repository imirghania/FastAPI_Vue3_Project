from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from functools import lru_cache
from core.config import Settings
from models import Product
from database import create_db_and_tables, get_session
from schemas import ProductCreate, ProductRead, ProductUpdate, OrderBase
from sqlmodel import Session, select
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:5174"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@lru_cache
def get_settings():
    return Settings()


@app.post("/products", response_model=ProductRead, 
            status_code=status.HTTP_201_CREATED)
def create(product: ProductCreate, session: Annotated[Session, Depends(get_session)]):
    product_db = Product.model_validate(product)
    session.add(product_db)
    session.commit()
    session.refresh(product_db)
    return product_db


@app.get("/products", response_model=list[ProductRead])
def get_all(session: Annotated[Session, Depends(get_session)]):
    stmt = select(Product)
    query = session.exec(stmt).all()
    return query


@app.get("/products/{id}", response_model=ProductRead)
def get_one(id:int, session: Annotated[Session, Depends(get_session)]):
    product = session.get(Product, id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found.")
    return product


@app.post("/products/buy", response_model=ProductRead)
def buy_one(payload: OrderBase, 
            session: Annotated[Session, Depends(get_session)]):
    
    product_db = session.get(Product, payload.id)
    if not product_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found.")
    product_db.quantity -= payload.quantity
    
    session.add(product_db)
    session.commit()
    session.refresh(product_db)
    
    return product_db


@app.patch("/products/{id}", response_model=ProductRead)
def update(id:int, 
        payload: ProductUpdate, 
        session: Annotated[Session, Depends(get_session)]):
    
    product_db = session.get(Product, id)
    if not product_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found.")
    payload_data = payload.model_dump(exclude_unset=True)
    product_db.sqlmodel_update(payload_data)
    
    session.add(product_db)
    session.commit()
    session.refresh(product_db)
    
    return product_db


@app.delete("/products/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete(id:int, session: Annotated[Session, Depends(get_session)]):
    
    product_db = session.get(Product, id)
    if not product_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product does not exist.")
    
    session.delete(product_db)
    session.commit()
    
    return {"msg": "Product Deleted"}



if __name__ == "__main__":
    create_db_and_tables()