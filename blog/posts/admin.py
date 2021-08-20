from django.contrib import admin

from .models import Post, Comment, PostComment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "text")
    search_fields = ("text",)
    empty_value_display = "-пусто-"

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "text")
    search_fields = ("text",)
    empty_value_display = "-пусто-"

admin.site.register(Comment, CommentAdmin)


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "post")
    search_fields = ("text",)
    empty_value_display = "-пусто-"
    
admin.site.register(PostComment, PostCommentAdmin)


