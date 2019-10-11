from django.db import models

# Create your models here.
class CategoryLinks(models.Model):
  url = models.CharField(max_length=200)
  name = models.CharField(max_length=100)
  shop_id = models.IntegerField()

class ProductCategoryPages(models.Model):
  url = models.CharField(max_length=200)
  shop_id = models.IntegerField()
  img_url = models.CharField(max_length=200)
  title = models.CharField(max_length=100)
  price = models.IntegerField()