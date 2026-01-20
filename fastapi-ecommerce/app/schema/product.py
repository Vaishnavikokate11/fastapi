from pydantic import BaseModel, Field
from typing import Annotated

class Product(BaseModel):
    id: str
    sku: Annotated[str, Field
                   (min_length=8, max_length=30, title="SKU", description="Stock keeping unit",
                    example="359-hjd-453-3d"),
                    ]
    name: str


