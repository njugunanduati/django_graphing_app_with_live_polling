import json
from django.http import Http404
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class RandomNumberList(APIView):
    """
    A list of random numbers.
    """
    def get(self, request):
        number = 1000
        try:
            numbers = [i for i in range(number) if i % 3 == 0 and i % 5 == 0 ]
            result = {"status": status.HTTP_200_OK, "message": numbers}
        except Exception as e:
            result = {"status": status.HTTP_400_BAD_REQUEST, "message": str(e)}
        return Response(result)
