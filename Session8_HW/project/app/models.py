from django.db import models
from datetime import date
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateField(auto_now_add=True, null=True)
    date_deadline = models.DateField(null=True)

    def remaining_days(self):
        delta = self.date_deadline - date.today()
        days = delta.days
        return days

    def __str__(self):
        return self.title, self.content, self.date_created, self.date_deadline

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()