from typing import Optional
from decimal import Decimal
from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(default=None)
    price: Decimal = Field(max_digits=5, decimal_places=2)
    quantity: int
