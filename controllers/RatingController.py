from services.RatingService import RatingService

class RatingController:
    def __init__(self):
        self.rating_service = RatingService()

    def rating(self, id, data):
        return self.rating_service.new_or_update_rating(id, data)