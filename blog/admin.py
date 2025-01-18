from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'content', 'created_at', 'published')
    list_filter = ('title', 'content', 'created_at')
    search_fields = ('title', 'content')
