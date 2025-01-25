from django.shortcuts import render
from .models import Category, News


# Create your views here.

def home_page(request):
    news = News.objects.all()
    categories = Category.objects.all()

    context = {'news': news, 'categories': categories}

    return render(request, 'home.html', context)

