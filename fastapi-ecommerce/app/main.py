

from pathlib import Path
from fastapi import FastAPI, HTTPException, Query
from service.products import get_all_products

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Welcome to the fastapi series!"}

# @app.get("/products/{id}")
# def get_product(id: int):
#     products = ["Laptop", "Mouse", "Keyboard"]
#     return (
#         products[id]
#         if products[id]
#         else HTTPException(status_code=404, detail="Product not found")
#         )

# 
@app.get("/products")
def list_products(
    name: str = Query(
    default="",
    min_length=0, 
    max_length=50, 
    description= "Search prodcuts by name (case insensitive)",
    ),
    sort_by_price: bool = Query(
        default=False,
        description="Sort products by price "
    ),
    order: str = Query(
        default="asc",
        description= "Order od sorting (asc, desc)"
    ),

    limit : int =  Query(
    default=10,
    ge = 1, 
    le= 100, 
    description= "number of products to return",
    ),

     offset : int =  Query(
    default=0,
    ge = 1,  
    description= "paggination",
    ),
    ):
    products = get_all_products()

    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

        if not products:
            raise HTTPException(
                status_code=404, detail = f"No product found"
                )

        if sort_by_price:
            reverse = order == "desc"
            products = sorted(products, key=lambda p:p.get("price",0), reverse=reverse)
    
    total = len(products)
    #products = products[0:limit]
    products = products[offset: offset + limit]
    return { "total" : total, "items": products}

@app.get("/products/{product_id}")
def get_product_by_id(product_id: str = Path
(
    ..., 
    min_length = 36,
    max_length = 36,
    description = "UUID of products",
    example = "a0752149-a1c8-498c-98b2-7c40844346dsh"
)
):
    products = get_all_products()
    for product in products:
        if product.get("id") == product_id:
            return product
    raise HTTPException(status_code=404, detail="product not found")