from services.AuthenticationService import AuthenticationService

class AuthenticationController:
    def __init__(self):
        self.authentication_service = AuthenticationService()

    def login(self, request):
        data = request.json
        return self.authentication_service.login(data)

    def register(self, request):
        data = request.json
        return self.authentication_service.register(data)