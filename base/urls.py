from django.urls import path

from .views import base_views, board_views, comment_views, vote_views

app_name = 'base'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:board_id>/', base_views.detail, name='detail'),

    # board_views.py
    path('board/create/', board_views.board_create, name='board_create'),
    path('board/modify/<int:board_id>/', board_views.board_modify, name='board_modify'),
    path('board/delete/<int:board_id>/', board_views.board_delete, name='board_delete'),

    # comment_views.py
    path('comment/create/<int:board_id>', comment_views.comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>/', comment_views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', comment_views.comment_delete, name='comment_delete'),

    # reply
    path('comment/reply/create/<int:comment_id>', comment_views.reply_create, name='reply_create'),
    path('comment/reply/modify/<int:reply_id>', comment_views.reply_modify, name='reply_modify'),
    path('comment/reply/delete/<int:reply_id>', comment_views.reply_delete, name='reply_delete'),

    # vote_views.py
    path('vote/board/<int:board_id>/', vote_views.vote_board, name='vote_board'),
]