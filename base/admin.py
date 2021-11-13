from django.contrib import admin
from .models import Boards, Comment, Reply, Category

@admin.register(Boards)
class BoardsAdmin(admin.ModelAdmin):
    search_fields = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)