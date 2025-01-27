from django.shortcuts import render
from .models import Category, News


# Create your views here.

def home_page(request):
    news = News.objects.all()
    categories = Category.objects.all()

    context = {'news': news, 'categories': categories}

    return render(request, 'home.html', context)



def category_page(request, pk):

    category = Category.objects.get(id=pk)

    news = News.objects.filter(news_category=category)

    context = {'category': category, 'news': news}

    return render(request, 'category.html', context)



def news_page(request, pk):

    news = News.objects.get(id=pk)

    context = {'news': news}

    return render(request, 'news.html', context)
