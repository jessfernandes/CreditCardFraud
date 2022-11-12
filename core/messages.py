class CoreMessage:
    _invalid_input = "Invalid input format"
    _server_error = "Internal server error"

    @property
    def invalid_input(self) -> str:
        return self._invalid_input

    @property
    def server_error(self) -> str:
        return self._server_error
