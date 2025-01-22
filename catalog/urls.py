from config.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path('home/', views.home, name='home')
    ]
