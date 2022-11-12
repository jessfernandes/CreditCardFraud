from django.http import response
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.db.utils import DatabaseError
from rest_framework.views import APIView
from rest_framework import status
from core.utils import error_response, response
from user.messages import Message
from user.serializers import (
    UserModelSerializer,
    UserUpdateSerializer,
)


class UserView(APIView):
    """Endpoints to manage users."""
    message = Message()

    def get(self, request: HttpRequest) -> HttpResponse:
        """List all users."""
        try:
            username = username = request.user
            users = User.objects.get(username=username)
            user_serializer = UserModelSerializer(users)
            return response(user_serializer.data, status.HTTP_200_OK)
        except Exception:
            return error_response(10, self.message.server_error,
                                  status.HTTP_500_INTERNAL_SERVER_ERROR)
            

    def put(self, request: HttpRequest) -> HttpResponse:
        """Updates a specific user."""
        user_serializer = UserUpdateSerializer(data=request.data)
        if user_serializer.is_valid():
            try:
                if str(request.user) == str(user_serializer.data["username"]):
                    user = User.objects.get(username=user_serializer.data["username"])
                    if (user_serializer.data["password"] ==
                            user_serializer.data["confirm_password"]):
                        user.username = user_serializer.data["username"]
                        user.email = user_serializer.data["email"]
                        user.set_password(raw_password=user_serializer.data["password"])
                        user.save()
                        user_model_serializer = UserModelSerializer(user)
                        return response(user_model_serializer.data,
                                        status.HTTP_200_OK)
                    return error_response(13,
                                        self.message.invalid_confirm_password,
                                        status.HTTP_400_BAD_REQUEST)
                else:
                    return error_response(14, self.message.user_not_current,
                                      status.HTTP_400_BAD_REQUEST)
            except DatabaseError:
                return error_response(14, self.message.update_error,
                                      status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Exception:
                return error_response(15, self.message.server_error,
                                      status.HTTP_500_INTERNAL_SERVER_ERROR)
        return error_response(16, self.message.invalid_input,
                              status.HTTP_400_BAD_REQUEST)