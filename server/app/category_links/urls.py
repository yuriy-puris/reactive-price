from django.urls import path

from .views import CategoryLinksView, ProductCategoryView

urlpatterns = [
  path('/category', CategoryLinksView.as_view(), name='category'),
  path('/product_category', ProductCategoryView.as_view(), name='product_category')
]