from extensions import db

class Rating(db.Model):
    __tablename__ = "rating"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    movie_serie_id = db.Column(db.Integer, db.ForeignKey("movie_serie.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return "<Rating %r>" % self.rating

    def serialize(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "user_id": self.user_id,
            "movie_serie_id": self.movie_serie_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }