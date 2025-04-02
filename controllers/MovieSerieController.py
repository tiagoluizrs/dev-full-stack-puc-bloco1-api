from models.MovieSerie import MovieSerie

class MovieSerieController:
    def get_all(self):
        movies_series = MovieSerie.query.all()
        return [movie_serie.serialize() for movie_serie in movies_series]

    def get_by_id(self, id):
        movie_serie = MovieSerie.query.filter_by(id=id).first()
        return movie_serie.serialize() if movie_serie else {}

    def create(self, data):
        pass

    def update(self, id, data):
        movie_serie = MovieSerie.query.filter_by(id=id).first()
        if not movie_serie:
            return {"message": "Movie/Serie not found"}, 404

        for key, value in data.items():
            setattr(movie_serie, key, value)
        movie_serie.save()

    def delete(self, id):
        MovieSerie.query.filter_by(id=id).delete()
        return {"message": "Movie/Serie deleted successfully"}

        return rating.serialize()