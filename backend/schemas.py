from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, Field
from sqlmodel import SQLModel


class BaseProduct(BaseModel):
    name: str
    description: Optional[str] = Field(default=None)
    price: Decimal
    quantity: int


class ProductCreate(BaseProduct):
    pass


class ProductRead(BaseProduct):
    id: int

class ProductUpdate(SQLModel):
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    price: Optional[Decimal] = Field(default=None)
    quantity: Optional[int] = Field(default=None)

class OrderBase(BaseModel):
    id: int
    quantity: int