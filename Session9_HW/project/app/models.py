from django.db import models
from django.contrib.auth.models import User
from datetime import date
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, default=None)
    content = models.TextField(default=None)
    date_created = models.DateField(auto_now_add=True, null=True)
    date_deadline = models.DateField(default=None)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True, related_name='posts')

    def remaining_days(self):
        delta = self.date_deadline - date.today()
        days = delta.days
        return days

    def __str__(self):
        return '{} {} {} {} {}'.format(self.title, self.content, self.date_created, self.date_deadline, self.author)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', default=None)
    content = models.TextField(default=None)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True, related_name='comments')
