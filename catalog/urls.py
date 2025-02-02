from catalog import views
from config.urls import path

app_name = 'catalog'

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path('home/', views.home, name='home'),
    path('example/', views.example_view, name='example'),
    path('index/', views.index, name='index'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('product_list/', views.product_list, name='product_list'),
    path('base_test/', views.base_test, name='base_test')

    ]
