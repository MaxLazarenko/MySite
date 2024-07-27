from django.shortcuts import render
from .models import New

# Create your views here.

def home(request):
    data = {
        'news': New.objects.all(),
        'title': 'Главная страница'
    }
    return render(request, 'blog/home.html', data)

def contacts(request):
    return render(request, 'blog/contacts.html',{'title': 'Страничка про семью'})