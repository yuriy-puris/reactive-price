from django.db import models

# Create your models here.
class CategoryLinks(models.Model):
  url = models.CharField(max_length=200)
  name = models.CharField(max_length=100)
  shop_id = models.IntegerField()