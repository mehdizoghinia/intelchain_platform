from django.urls import path
from .views import (
    ProductListCreateAPIView,
    ProductDetailAPIView,
    BusinessListCreateAPIView,
    BusinessDetailAPIView,
    AddProductToBusinessAPIView,
)

urlpatterns = [
    path("products/", ProductListCreateAPIView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
    path("", BusinessListCreateAPIView.as_view(), name="business-list-create"),
    path("<int:pk>/", BusinessDetailAPIView.as_view(), name="business-detail"),
    path(
        "<int:pk>/add_product/",
        AddProductToBusinessAPIView.as_view(),
        name="add-product-to-business",
    ),
]
