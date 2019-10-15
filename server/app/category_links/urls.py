from django.urls import path

from .views import CategoryLinksView

urlpatterns = [
  path('category', CategoryLinksView.as_view(), name='category')
]