from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (BlogCreateView, BlogListView, BlogDetailView,
                    BlogUpdateView, BlogDeleteView, BlogContactsTemplateView)


app_name = 'blog'

urlpatterns = [

    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    path('contacts/', BlogContactsTemplateView.as_view(), name='contacts')

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
