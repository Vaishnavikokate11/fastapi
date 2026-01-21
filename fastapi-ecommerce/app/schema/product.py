from uuid import UUID
from pydantic import BaseModel, Field
from typing import Annotated

class Product(BaseModel):
    id: UUID
    sku: Annotated[str, Field
                   (min_length=8, max_length=30, title="SKU", description="Stock keeping unit",
                    example=["359-hjd-453-3d"]
                    ),
                    ]
    name: Annotated[
        str,
        Field(
            min_length=3,
            max_length=80,
            title= "Product name",
            description="Readable product name",
            example= ["Lenovo Model Max"]
        )
    ]

    description: Annotated[
        str, Field(
            min_length=3,
            max_length=80,
            title= "Description",
            description="Readable description",
            example= ["Official Lenovo product with manufacturer warranty"]

        )
    ]

    category: Annotated[
        str, Field(
            min_length=3,
            max_length=80,
            title= "categories",
            description="Radable category",
            example= ["accessories"]

        )
    ]
    brand: Annotated[
        str, Field(
            min_length=3,
            max_length=80,
            title= "Brands",
            description="Readable brands",
            example= ["Lenovo"]

        )
    ]

    price: Annotated [ 
        int, Field(
            min_length=3,
            max_length=80,
            title= "Price",
            description="Readable price",
            example= ["104946.0"]

        )
    ]

    currency: Annotated [ 
        str, Field(
            min_length=3,
            max_length=80,
            title= "Currency",
            description="Readable currency",
            example= ["INR"]

        )
    ]

    discount_percent: Annotated [ 
        int, Field(
            min_length=3,
            max_length=80,
            title= "Discount percent",
            description="Readable Discount",
            example= ["20"]

        )
    ]

    stock: Annotated [ 
        int, Field(
            min_length=3,
            max_length=80,
            title= "stock",
            description="Readable stock",
            example= ["122"]

        )
    ]
    is_active: Annotated [ 
        bool, Field(
            min_length=3,
            max_length=80,
            title= "Active account",
            description="Acount active or not",
            example= ["true"]

        )
    ]

    rating: Annotated [ 
        float, Field(
            min_length=3,
            max_length=80,
            title= "Rating",
            description="Rating for product",
            example= ["true"]

        )
    ]
    
    


    



