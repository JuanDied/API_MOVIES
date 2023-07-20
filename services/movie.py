from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movie_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.genre == category).all()
        return result
    
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return  new_movie
    
    def update_movie(self, id: int, movie: Movie):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            return None
        result.title = movie.title
        result.director = movie.director
        result.year = movie.year
        result.overview = movie.overview
        result.rating = movie.rating
        result.genre = movie.genre
        self.db.commit()
        return result
    
    def delete_movie(self, id: int):
        result = self.get_movie(id)
        if not result:
            return None
        self.db.delete(result)
        self.db.commit()
        return result