from rest_framework import generics
from .models import CategoryLinks
from .serializers import CategoryLinksSerializer

class CategoryLinksView(generics.ListAPIView):
  queryset = CategoryLinks.objects.all()
  serializer_class = CategoryLinksSerializer