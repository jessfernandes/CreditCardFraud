from typing import Dict
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse, HttpRequest
from rest_framework import status
from core.utils import error_response, response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.exceptions import TokenError
from authentication.messages import Message
from authentication.serializers import (
    LoginSerializer,
    RenovationSerializer,
)


def _create_authentication_payload(refresh_token: RefreshToken) -> Dict[str,
                                                                        str]:
    return {
        "tk_renovation": str(refresh_token),
        "tk_access": str(refresh_token.access_token),
    }


@api_view(["POST"])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login(request: HttpRequest) -> HttpResponse:
    """Logs a user in."""
    message = Message()

    login_serializer = LoginSerializer(data=request.data)
    if login_serializer.is_valid():
        user = authenticate(
            username=login_serializer.data["username"],
            password=login_serializer.data["password"],
        )

        if user:
            refresh_token = RefreshToken.for_user(user)
            payload = _create_authentication_payload(refresh_token)
            return response(payload, status.HTTP_200_OK)

        return error_response(2, message.invalid_credentials,
                              status.HTTP_401_UNAUTHORIZED)
    return error_response(1, message.invalid_input,
                          status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def renovate(request: HttpRequest) -> HttpResponse:
    """Renovate the access token of a user."""
    message = Message()

    renovation_serializer = RenovationSerializer(data=request.data)
    if renovation_serializer.is_valid():
        try:
            refresh_token = RefreshToken(
                renovation_serializer.data["tk_renovation"]
            )
            payload = _create_authentication_payload(refresh_token)
            return response({"tk_access":payload['tk_access']}, status.HTTP_200_OK)
        except TokenError:
            return error_response(3, message.bad_renovation_token,
                                  status.HTTP_401_UNAUTHORIZED,True)
        except Exception:
            return error_response(4, message.server_error,
                                  status.HTTP_500_INTERNAL_SERVER_ERROR)
    return error_response(5, message.invalid_input,
                          status.HTTP_400_BAD_REQUEST)
