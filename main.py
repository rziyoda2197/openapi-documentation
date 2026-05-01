from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="OpenAPI Documentation Customization",
    description="Customizing OpenAPI documentation for our API",
    version="1.0.0",
    contact={
        "name": "John Doe",
        "email": "john.doe@example.com",
        "url": "https://example.com"
    },
    license={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    }
)

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users/")
async def read_users():
    return [{"id": 1, "name": "John Doe", "email": "john.doe@example.com"}]

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"id": user_id, "name": "John Doe", "email": "john.doe@example.com"}
```

```bash
uvicorn main:app --reload
```

```bash
curl http://localhost:8000/docs
```

```bash
curl http://localhost:8000/redoc
