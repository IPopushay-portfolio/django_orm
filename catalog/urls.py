from django.urls import path
from .views import home, contacts, products_detail


app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_detail/<int:pk>', products_detail, name='product_detail'),

    ]
