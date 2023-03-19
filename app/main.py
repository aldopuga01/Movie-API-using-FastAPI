from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from app.movies import movies_router
from app.models import User
from app.manager_token import create_token
from models.movie import Movie as MovieModel
from config.database import engine, Base

app = FastAPI(title='My API', description='My First API with fastAPI', version='1.0.0')

# Create the database
Base.metadata.create_all(bind = engine)

app.include_router(movies_router)

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse(content='<h1>My First API with fastAPI</h1>')

@app.post('/login', tags=['Login'])
def login(user: User):
    if user.username == 'admin' and user.password == 'admin':
        user_dict = {'username': user.username, 'password': user.password}
        token: str = create_token(user_dict)
        return JSONResponse(content=token, status_code=200)
    raise HTTPException(status_code=401, detail="Invalid username or password")


