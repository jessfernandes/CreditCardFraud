from django.http import response
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from core.utils import error_response, response
from core.messages import CoreMessage


class ClassificationView(APIView):
    """Endpoints to manage classification."""
    message = CoreMessage()

    def get(self, request: HttpRequest) -> HttpResponse:
        """Gets list of all predictions in the database."""
        try:
            error=0
            data_response={}
            if error == 0:
                return response(data_response, status.HTTP_200_OK)
            else:
                return error_response(11, data_response,
                                   status.HTTP_417_EXPECTATION_FAILED)
        except Exception:
            return error_response(11, CoreMessage().server_error,
                                   status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request: HttpRequest) -> HttpResponse:
        """Make a predictions based on a new sample."""
        try:
            error=0
            data_response={}
            if error == 0:
                return response(data_response, status.HTTP_200_OK)
            else:
                return error_response(12, data_response,
                                   status.HTTP_417_EXPECTATION_FAILED)
        except Exception:
            return error_response(12, CoreMessage().server_error,
                                   status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request: HttpRequest) -> HttpResponse:
        """Delete a register in the database."""
        try:
            error=0
            data_response={}
            if error == 0:
                return response(data_response, status.HTTP_200_OK)
            else:
                return error_response(13, data_response,
                                   status.HTTP_417_EXPECTATION_FAILED)
        except Exception:
            return error_response(13, CoreMessage().server_error,
                                   status.HTTP_500_INTERNAL_SERVER_ERROR)
