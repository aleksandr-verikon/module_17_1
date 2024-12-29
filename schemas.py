from pydantic import BaseModel

class CreateProduct(BaseModel):
    name: str
    description: str
    price: int
    image_url: str
    stock: str
    categoory: int

class CreateCategory(BaseModel):
    name: str
    parent_id: int
