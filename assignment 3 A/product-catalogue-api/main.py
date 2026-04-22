from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from bson import ObjectId
from models import ProductModel, UpdateProductModel
from database import collection

# Setup Limiter for Rate Limiting (Mandatory Guideline)
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="Product Catalogue API")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# POST /products (Rate limited: 20 per minute)
@app.post("/products", response_model=ProductModel, status_code=status.HTTP_201_CREATED)
@limiter.limit("20/minute")
async def create_product(request: Request, product: ProductModel):
    new_product = await collection.insert_one(product.model_dump())
    created_product = await collection.find_one({"_id": new_product.inserted_id})
    return created_product

# GET /products (With optional category filter)
@app.get("/products")
async def get_products(category: str = None):
    query = {}
    if category:
        query = {"category": category}
    
    products = []
    async for product in collection.find(query):
        product["id"] = str(product.pop("_id"))
        products.append(product)
    return products

# GET /products/{id}
@app.get("/products/{id}")
async def get_product(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=422, detail="Invalid ID format")
    
    product = await collection.find_one({"_id": ObjectId(id)})
    if product:
        product["id"] = str(product.pop("_id"))
        return product
    raise HTTPException(status_code=404, detail=f"Product {id} not found")

# DELETE /products/{id}
@app.delete("/products/{id}")
async def delete_product(id: str):
    delete_result = await collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Product {id} not found")