class CoreMessage:
    _empty_return = "There is no data in the database"
    _invalid_input = "Invalid input format"
    _invalid_input_value = "Invalid input value. Check it"
    _server_error = "Internal server error"
    _delete = "The register has been deleted succesfully"

    @property
    def empty_return(self) -> str:
        return self._empty_return
    
    @property
    def invalid_input(self) -> str:
        return self._invalid_input

    @property
    def invalid_input_value(self) -> str:
        return self._invalid_input_value

    @property
    def server_error(self) -> str:
        return self._server_error

    @property
    def delete(self) -> str:
        return self._delete
