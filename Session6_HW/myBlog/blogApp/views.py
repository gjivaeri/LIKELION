from django.shortcuts import render, redirect
from .models import Article, Category
from django.utils import timezone
# Create your views here.

def index(request):
    # movie_cnt = Article.objects.filter(category='movie').count()
    movie_cnt = Category.objects.filter(name='movie').count()
    drama_cnt = Category.objects.filter(name='drama').count()   
    programming_cnt = Category.objects.filter(name='programming').count()
    return render(request, 'index.html', {'movie_cnt': movie_cnt, 'drama_cnt': drama_cnt, 'programming_cnt': programming_cnt})

def detail(request, article_pk): 
    article = Article.objects.get(pk=article_pk)
    return render(request, 'detail.html', {'article' : article})

def movie(request):
    movie = Category.objects.get(name="movie")
    movies = Article.objects.filter(category=movie)
    return render(request, 'movie.html', {'articles' : movies})

def drama(request):
    drama = Category.objects.get(name="drama")
    dramas = Article.objects.filter(category=drama)
    return render(request, 'drama.html', {'articles' : dramas})

def programming(request):
    programming = Category.objects.get(name="programming")
    programmings = Article.objects.filter(category=programming)
    return render(request, 'programming.html', {'articles' : programmings})

def new(request):
    if request.method == 'POST' :
        time = timezone.localtime()
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            time=time
        )
        return redirect('detail', article_pk=new_article.pk)

    return render(request, 'new.html')
