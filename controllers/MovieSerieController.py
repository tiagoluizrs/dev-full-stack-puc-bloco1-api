from datetime import datetime

from extensions import db
from models.MovieSerie import MovieSerie

class MovieSerieController:
    def get_all(self, page=1, limit=10, type=None):
        query = MovieSerie.query

        if type:
            query = query.filter_by(type=type)

        query = query.paginate(page=page, per_page=limit, error_out=False)
        return {
            'items': [item.serialize() for item in query.items],
            'total': query.total,
            'page': query.page,
            'pages': query.pages
        }

    def get_by_id(self, id):
        movie_serie = MovieSerie.query.filter_by(id=id).first()
        return movie_serie.serialize() if movie_serie else {}

    def create(self, data):
        movie_serie = MovieSerie(
            title=data["title"],
            synopsis=data["synopsis"],
            classification=data["classification"],
            duration=data["duration"] if "duration" in data.keys() else None,
            chapters=data["chapters"] if "chapters" in data.keys() else None,
            seasons=data["seasons"] if "seasons" in data.keys() else None,
            director=data["director"],
            genre=data["genre"],
            image=data["image"],
            release_date=datetime.strptime(data["release_date"], '%Y-%m-%d').date() if data["release_date"] else None,
            type=data["type"]
        )
        db.session.add(movie_serie)
        db.session.commit()

        return movie_serie.serialize()