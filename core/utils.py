from typing import Any
from django.http import HttpResponse
from rest_framework.response import Response


def error_response(code: int, msg: str, status_response: int, error:bool=False) -> HttpResponse:
    if error: return Response(data={"msg":msg, "error":code},status=status_response)
    else: return Response(data={"msg":msg},status=status_response)


def response(data: Any,
             status_response: int,
             error_code: int = 0) -> Response:
    return Response(data=data,status=status_response)
