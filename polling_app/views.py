import json
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.views.generic import TemplateView



class RandomNumberList(generics.ListAPIView):
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



class HomeView(TemplateView):
    template_name = 'index.html'
