from django.http import response
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from core.utils import error_response, response
from core.messages import CoreMessage
from classification.models import predict
from classification.utils.classification import Classification
import json

class ClassificationView(APIView):
    """Endpoints to manage classification."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Gets list of all predictions in the database."""
        try:

            data = predict.objects.all().extra(select={'id':'id','class':'class_predicted','probability':'probability'}).values('id','class_predicted','probability')
            if data:
                return response(data, status.HTTP_200_OK)
            else:
                return error_response(11, CoreMessage().empty_return, status.HTTP_200_OK)
        except Exception:
            return error_response(11, CoreMessage().server_error,
                                   status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request: HttpRequest) -> HttpResponse:
        """Make predictions based on a new sample."""
        try:
            try: data_inp = json.loads(request.body.decode("utf-8"))
            except: data_inp = request.data

            data_response, error = Classification(data_inp).fit()

            if error == 0:
                return response(data_response, status.HTTP_200_OK)
            else:
                return error_response(12, data_response,
                                   status.HTTP_417_EXPECTATION_FAILED)
        except Exception as e:
            return error_response(12, CoreMessage().server_error,
                                   status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request: HttpRequest) -> HttpResponse:
        """Delete a register in the database."""
        try:

            try: data = json.loads(request.body.decode("utf-8"))
            except: data = request.data

            if 'id' in data.keys():
                try:
                    pred_db = predict.objects.get(id=data['id'])
                    feat_db = pred_db.featuresid

                    pred_db.delete()
                    feat_db.delete()

                    return error_response(13,CoreMessage().delete, status.HTTP_200_OK)
                except:
                    return error_response(13, CoreMessage().invalid_input_value,
                                   status.HTTP_417_EXPECTATION_FAILED)
        except Exception:
            return error_response(13, CoreMessage().server_error,
                                   status.HTTP_500_INTERNAL_SERVER_ERROR)
