
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
    default=None,
    min_length=1, 
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
    ):
    products = get_all_products()

    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

        if not products:
            raise HTTPException(
                status_code=404, detail = f"No product found"
                )
    
    total = len(products)
    return { "total" : total, "items": products}
