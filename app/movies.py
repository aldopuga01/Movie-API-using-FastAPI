from fastapi import APIRouter, Body, Path, Query, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from app.models import JWTBearer, Movie
from config.database import Session
from models.movie import Movie as MovieModel

movies_router = APIRouter()

movies = [
    {'id': 1, 'name': 'The Shawshank Redemption', 'year': 1994, 'genre': 'Drama'},
    {'id': 2, 'name': 'The Godfather', 'year': 1972, 'genre': 'Drama'},
    {'id': 3, 'name': 'The Godfather: Part II', 'year': 1974, 'genre': 'Drama'},
    {'id': 4, 'name': 'The Dark Knight', 'year': 2008, 'genre': 'Action'},
    {'id': 5, 'name': '12 Angry Men', 'year': 1957, 'genre': 'Drama'}
]

# Retornar todas las peliculas
@movies_router.get('/movies/all', tags=['Movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    return movies

@movies_router.get('/movies/{id}', tags=['Movies'], response_model=Movie)
def find_by_id(id: int = Path(default=1, ge=1, le=len(movies))) -> Movie:
    # Realizar filtrado por id utilizando el parámetro path utilizando try y except
    try:
        movie = [movie for movie in movies if movie['id'] == id][0]
        return movie
    except IndexError: 
        raise HTTPException(status_code=404, detail='Movie not found')

@movies_router.get('/movies', tags=['Movies'], response_model=List[Movie])
def find_by_genre(genre: Optional[str] = Query(None, min_length=3, max_length=100)) -> List[Movie]: 
    # Realizar filtrado por genero utilizando el parámetro query utilizando try y except
    try:
        filtered_movies = [movie for movie in movies if movie['genre'] == genre]
        return filtered_movies
    except IndexError:
        raise HTTPException(status_code=404, detail='Movie not found')

@movies_router.post('/movies', tags=['Movies'], response_class=JSONResponse)
def create_movie(movie: Movie) -> JSONResponse:
    # Crear sesion de base de datos
    session = Session()
    # Crear objeto de tipo MovieModel como diccionario
    movie_model = MovieModel(**movie.dict())
    # Agregar objeto a la base de datos
    session.add(movie_model) 
    # Guardar cambios en la base de datos
    session.commit()
    return JSONResponse(content={'message': 'Movie created successfully'})

@movies_router.put('/movies/{id}', tags=['Movies'], response_class=JSONResponse)
def update_movie(id: int, movie: Movie) -> JSONResponse:
    try:
        movie_dict = [movie for movie in movies if movie['id'] == id][0]
        movie_dict['name'] = movie.name
        movie_dict['year'] = movie.year
        movie_dict['genre'] = movie.genre
        return JSONResponse(content={'message': 'Movie updated successfully'})
    except IndexError:
        raise HTTPException(status_code=404, detail='Movie not found')

@movies_router.delete('/movies/{id}', tags=['Movies'], response_class=JSONResponse)
def delete_movie(id: int) -> JSONResponse:
    try:
        movie = [movie for movie in movies if movie['id'] == id][0]
        movies.remove(movie)
        return JSONResponse(content={'message': 'Movie deleted successfully'})
    except IndexError:
        raise HTTPException(status_code=404, detail='Movie not found')
