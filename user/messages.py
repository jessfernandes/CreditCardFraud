from core.messages import CoreMessage


class Message(CoreMessage):
    _user_not_current = "It is just allowed to update you user. Check it!"
    _user_not_found = "User not found"
    _create_error = "Error while creating the new user"
    _update_error = "Error while updating the user data"
    _delete_error = "Error while deleting the user"
    _invalid_confirm_password = "Confirm password does not match password"
    _delete_success = "User successfully deleted"

    @property
    def user_not_current(self) -> str:
        return self._user_not_current

    @property
    def user_not_found(self) -> str:
        return self._user_not_found

    @property
    def create_error(self) -> str:
        return self._create_error

    @property
    def update_error(self) -> str:
        return self._update_error

    @property
    def delete_error(self) -> str:
        return self._delete_error

    @property
    def invalid_confirm_password(self) -> str:
        return self._invalid_confirm_password

    @property
    def delete_success(self) -> str:
        return self._delete_success
