from rest_framework import serializers
from .models import CategoryLinks, ProductCategoryPages

class CategoryLinksSerializer(serializers.ModelSerializer):
  class Meta:
    model = CategoryLinks
    fields = ('url', 'name', 'shop_id')

class ProductCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductCategoryPages
    fields = ('url', 'shop_id', 'img_url', 'title', 'price')