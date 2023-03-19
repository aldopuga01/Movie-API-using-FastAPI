from fastapi import HTTPException, Request
from pydantic import BaseModel, Field 
from typing import Optional
from fastapi.security import HTTPBearer
from .manager_token import validate_token
from datetime import datetime

class Movie(BaseModel):
    id: Optional[int] = None
    name: str = Field(default="Mi pelicula", max_length=100)
    # Validar que el año no sea mayor al año actual
    year: int = Field(le=datetime.now().year)  
    genre: str = Field(default="Acción",max_length=100)

    class Config:
        schema_extra = {
            "example": {
                "name": "Back to the Future",
                "year": 1985,
                "genre": "Comedy"
            }
        }

class User(BaseModel):
    username: str = Field(default=" ", max_length=100)
    password: str = Field(default=" ", max_length=100)

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['username'] != 'admin':
            raise HTTPException(status_code=401, detail='Invalid username')
        return auth.credentials
