from uuid import UUID
from pydantic import BaseModel, Field, AnyUrl, field_validator, model_validator, computed_field
from typing import Annotated, List, Literal, Optional
from datetime import datetime

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
        ),
    ]

    description: Annotated[
        str, Field(
            min_length=3,
            max_length=80,
            title= "Description",
            description="Readable description",
            example= ["Official Lenovo product with manufacturer warranty"]

        ),
    ]

    category: Annotated[
        str, Field(
            min_length=3,
            max_length=80,
            title= "categories",
            description="Radable category",
            example= ["accessories"]

        ),
    ]
    brand: Annotated[
        str, Field(
            min_length=3,
            max_length=80,
            title= "Brands",
            description="Readable brands",
            example= ["Lenovo"]

        ),
    ]

    price: Annotated [ 
        float, Field(
            ge=0,
            strict=True,
            description="Base price (INR)",
            

        ),
    ]

    currency: Literal["INR"]= "INR"

    discount_percent: Annotated [ 
        int, Field(
            ge=0,
            le=90,
            description="Discount in percent (0-90)"

        ),
    ]

    stock: Annotated [ 
        int, Field(
            ge=0,
            description="Available stock (>=0)"

        ),
    ]
    is_active: Annotated [ 
        bool, Field(
            description="Is stock active"

        ),
    ]

    rating: Annotated [ 
        float, Field(
            ge=0,
            le=5,
            strict=True,
            description="Rating for product"
    
        ),
    ]

    tags: Annotated[ Optional[List[str]],
         Field(
            default=None,
            max_length=10,
            description="Upto 10 tags"
    
        ),
    ]

    image_urls: Annotated [List[AnyUrl],
         Field(
            max_length=1,
            description="atleast one image url"
    
        ),
    ]

    #dimesions_c,
    #seller
    created_at: datetime

    @field_validator("sku", mode="after")

    @classmethod
    def validate_sku_format(cls, value:str):
        if "-" not in value:
            raise ValueError("Sku must have '-'")
        
        last = value.split("-")[-1]
        if not (len(last)==3 and last.isDigit()):
            raise ValueError("Sku end with a 3 digit sequence like -321")
        return value
    
    


    



