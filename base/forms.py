from django import forms
from base.models import Boards, Comment, Reply, Category

class BoardForm(forms.ModelForm):
    class Meta:
        model = Boards
        fields = ['category', 'title', 'content']
        labels = {
            'category': '분류',
            'title': '제목',
            'content': '내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }