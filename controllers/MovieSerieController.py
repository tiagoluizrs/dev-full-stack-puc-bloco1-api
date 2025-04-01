from services.MovieSerieService import MovieSerieService

class MovieSerieController:
    def __init__(self):
        self.movie_serie_service = MovieSerieService()

    def get_all(self):
        return self.movie_serie_service.get_all()

    def get_by_id(self, id):
        return self.movie_serie_service.get_by_id(id)

    def create(self, data):
        return self.movie_serie_service.create(data)

    def update(self, id, data):
        return self.movie_serie_service.update(id, data)

    def delete(self, id):
        return self.movie_serie_service.delete(id)