from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_name', 'content',)
    list_filter = ('blog_name',)
    search_fields = ('blog_name', 'content')
