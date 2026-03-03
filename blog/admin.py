from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_filter = ('email',)
    search_fields = ('username',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("created_time", "post", "content")
    list_filter = ("post",)
    search_fields = ("content",)

admin.site.unregister(Group)
