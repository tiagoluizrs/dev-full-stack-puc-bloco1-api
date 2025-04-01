from extensions import db
from sqlalchemy import func

class MovieSerie(db.Model):
    __tablename__ = "movie_serie"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.String(10), nullable=True)
    chapters = db.Column(db.Integer, nullable=True)
    seasons = db.Column(db.Integer, nullable=True)
    classification = db.Column(db.String(4), nullable=False, default="Free")
    synopsis = db.Column(db.Text, nullable=False)
    director = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Integer, nullable=False, default=1)
    status = db.Column(db.Boolean, nullable=False, default=True)
    image = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return "<MovieSerie %r>" % self.title

    def serializer(self):
        from models.Rating import Rating
        average_rating = db.session.query(func.avg(Rating.rating)).filter(Rating.movie_serie_id == self.id).scalar()

        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
            "duration": self.duration,
            "chapters": self.chapters,
            "seasons": self.seasons,
            "classification": self.classification,
            "synopsis": self.synopsis,
            "director": self.director,
            "genre": self.genre,
            "type": self.type,
            "status": self.status,
            "image": self.image,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "average_rating": average_rating
        }