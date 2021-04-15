from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

class Article(models.Model): 
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField(max_length=300, null=False)
    time = models.TextField(default=timezone.localtime())

    def __str__(self):
        return self.title