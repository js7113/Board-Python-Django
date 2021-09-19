from django.contrib import admin
from .models import Boards, Comment, Reply


class BoardsAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Boards, BoardsAdmin)

admin.site.register(Comment)

admin.site.register(Reply)