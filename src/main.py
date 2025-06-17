A especificação está pedindo uma API em NodeJS, mas as instruções iniciais pedem em Python FastAPI. Vou assumir que é um erro e que você deseja uma API em FastAPI. Aqui está:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

items = {}

@app.post("/items/")
async def create_item(item: Item):
    """Create a new item."""
    if item.name in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.name] = item
    return item

@app.get("/items/{item_name}")
async def read_item(item_name: str):
    """Get an item by name."""
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_name]