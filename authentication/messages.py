from core.messages import CoreMessage


class Message(CoreMessage):
    _invalid_credentials = "Username or password is incorrect"
    _bad_renovation_token = "The renovation token is invalid or has expired"

    @property
    def invalid_credentials(self) -> str:
        return self._invalid_credentials

    @property
    def bad_renovation_token(self) -> str:
        return self._bad_renovation_token
