from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view()
def index(request):
    return Response("Welcome")

@api_view()
def lemons(request):
    return Response("list of lemons", status=status.HTTP_200_OK)