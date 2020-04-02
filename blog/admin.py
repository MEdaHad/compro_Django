from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'slug', 'created_on')
    list_filter = ("created_on",)
    search_fields = ['title', 'created_on']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)