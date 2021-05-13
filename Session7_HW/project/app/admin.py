from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = 'title', 'content', 'date_created', 'date_deadline'
    list_filter = ['date_deadline']

admin.site.register(Post, PostAdmin)