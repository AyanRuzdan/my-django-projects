from django.urls import path
from .views import ProductView

urlpatterns = [
    path('product/', ProductView.as_view(), name='add_product'),
    path('product/<int:product_id>/', ProductView.as_view(), name='edit_product'),
]
