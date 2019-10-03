from rest_framework import serializers
from .models import CategoryLinks

class CategoryLinksSerializer(serializers.ModelSerializer):
  class Meta:
    model = CategoryLinks
    fields = ('url', 'name', 'shop_id')