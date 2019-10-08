import requests
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoryLinks
from .serializers import CategoryLinksSerializer

class CategoryLinksView(APIView):

  def get(self, request, format=None):
    queryset = CategoryLinks.objects.all()
    serializer_class = CategoryLinksSerializer(queryset, many=True)
    return Response(serializer_class.data)

  def post(self, request, format=None):
    queryset = CategoryLinks.objects.all()
    serializer = CategoryLinksSerializer(queryset, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)