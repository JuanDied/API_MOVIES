from fastapi import APIRouter
from fastapi import  HTTPException, Path, Query, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()




@movie_router.get(
        '/movies', tags=['Movies'], response_model=List[Movie],
        status_code=status.HTTP_200_OK)
def get_movies()-> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result))

@movie_router.get("/movies/{movie_id}", tags=['Movies'], response_model=Movie)
def get_movie(movie_id: int = Path(ge=1, le=10000))-> Movie:
    db = Session()
    result = MovieService(db).get_movie(movie_id)
    if len(result) > 0:
        return JSONResponse(status_code= 200, content=jsonable_encoder(result[0]))
    raise HTTPException( detail="Movie not found")

@movie_router.get("/movies/", tags=['Movies'], response_model=List[Movie])
def get_movie_by_category(category: str = Query(None, min_length=2, max_length=15)):
    db = Session()
    result = MovieService(db).get_movie_category(category)
    if len(result) > 0:
        return JSONResponse(status_code= 200, content=jsonable_encoder(result))
    raise HTTPException( detail="No movies of this kind :(")


@movie_router.post("/movies", tags=['Movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie)-> dict:
    db = Session()
    new_movie = MovieService(db).create_movie(movie)
    return JSONResponse(content=jsonable_encoder(new_movie), status_code=201)
    


@movie_router.put("/movies/{id}", tags=['Movies'], status_code=200)
async def update_movie(id: int, movie: Movie):
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    MovieService(db).update_movie(id, movie)
    return JSONResponse(content=jsonable_encoder(dict(result)), status_code=200)


@movie_router.delete("/movies/{id}", tags=['Movies'], status_code=200)
async def delete_movie(id: int):
    db = Session()
    result = MovieService(db).delete_movie(id)
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse( status_code=200, content={"message": "Movie deleted successfully"})
