from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view()
def index(request):
    return Response("Welcome")

@api_view()
def lemons(request):
    return Response("list of lemons", status=status.HTTP_200_OK)


class Orders():
    @staticmethod
    @api_view(['POST', 'GET'])
    def listOrders(request):
        return Response({'message': 'list of orders'}, 200)
    
class LemonView(APIView):
    def get(self, request, pk):
        return Response({'message': 'single lemon with an id of ' + str(pk)}, status=status.HTTP_200_OK)
    def put(self, request, pk):
        return Response({'title': request.data.get('title')}, status=status.HTTP_200_OK)