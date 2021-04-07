from django.shortcuts import render

# Create your views here.

def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    except_blank = len(text.replace(" ","").replace("\t",""))
    words = len(text.split(" "))
    return render(request, 'result.html', 
    {'total_len': total_len, 
    'except_blank': except_blank,
    'text': text,
    'words': words})