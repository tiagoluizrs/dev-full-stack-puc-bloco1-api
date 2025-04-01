from models.MovieSerie import MovieSerie
from models.Rating import Rating
from models.User import User

class RatingService:
    def new_or_update_rating(self, id, data):
        user = User.query.filter_by(id=data["user_id"]).first()
        if not user:
            return {"message": "User not found"}, 404

        movie_serie = MovieSerie.query.filter_by(id=id).first()
        if not movie_serie:
            return {"message": "Movie/Serie not found"}, 404

        rating = Rating.query.filter_by(user_id=data["user_id"], movie_serie_id=id).first()
        if not rating:
            rating = Rating()
            rating.user_id = data["user_id"]
            rating.movie_serie_id = id
        rating.rating = data["rating.py"]
        rating.comment = data["comment"]
        rating.save()