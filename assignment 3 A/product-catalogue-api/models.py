from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from bson import ObjectId

# Helper to handle MongoDB ObjectId as a string
class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return str(v)

class ProductModel(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    price: float = Field(..., gt=0)
    category: str = Field(...)
    stock: int = Field(default=0, ge=0)
    
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Wireless Mouse",
                "description": "Ergonomic 2.4G mouse",
                "price": 25.99,
                "category": "Electronics",
                "stock": 50
            }
        }
    )

class UpdateProductModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    stock: Optional[int] = None