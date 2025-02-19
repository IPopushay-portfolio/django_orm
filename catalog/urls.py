from django.urls import path
from . views import (ProductCreateView, ProductListView, ProductDetailView,
                     ProductUpdateView, ProductDeleteView)
from . views import ContactsTemplateView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'catalog'

urlpatterns = [

    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("product_detail/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("home/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"),
    path("home/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
