from django.contrib import admin
from django.urls import path
from blogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/movie', views.movie, name='movie'),
    path('index/drama', views.drama, name='drama'),
    path('index/programming', views.programming, name='programming'),
    path('new', views.new, name='new'),
    path('detail/<int:article_pk>', views.detail, name='detail'),
]