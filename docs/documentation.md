# FastAPI Item Management API Documentation

This is a simple API built with FastAPI for creating and retrieving items.

## Dependencies
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- Pydantic: Data validation and settings management using python type annotations.

To install these dependencies, run:
```
pip install fastapi uvicorn[standard] pydantic
```
## Models

### Item

```python
class Item(BaseModel):
    name: str
    description: str
    price: float
```
- **name**: A string that represents the name of the item. It's unique for each item.
- **description**: A string that represents the description of the item.
- **price**: A float that represents the price of the item.

## Endpoints

### POST /items/

Creates a new item.

#### Parameters

- **item**: A JSON object that represents an item.

#### Example

Request:

```bash
curl -X POST "http://localhost:8000/items/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\":\"Item1\",\"description\":\"This is an item\",\"price\":15.2}"
```

Response:

```json
{
  "name": "Item1",
  "description": "This is an item",
  "price": 15.2
}
```

### GET /items/{item_name}

Retrieves an item by its name.

#### Parameters

- **item_name**: A string that represents the name of the item.

#### Example

Request:

```bash
curl -X GET "http://localhost:8000/items/Item1" -H "accept: application/json"
```

Response:

```json
{
  "name": "Item1",
  "description": "This is an item",
  "price": 15.2
}
```

## Important Notes

- If you try to create an item with a name that already exists, the API will return a 400 status code with a message "Item already exists".
- If you try to retrieve an item with a name that doesn't exist, the API will return a 404 status code with a message "Item not found".