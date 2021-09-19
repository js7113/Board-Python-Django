from django.db import models
from django.contrib.auth.models import User

class Boards(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id_board')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_board')

    def __str__(self):
        return self.title

class Comment(models.Model):
    board = models.ForeignKey(Boards, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)


class Reply(models.Model):
    content = models.TextField(null=True)
    board = models.ForeignKey(Boards, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)