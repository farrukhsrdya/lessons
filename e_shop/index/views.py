from django.shortcuts import render
from .models import New, News


# Create your views here.

def home_page(request):

    ttttt = New.objects.all()
    rrrrr = News.objects.all()

    context = {'ttttt' : New, 'rrrrr': News}

    return render(request, 'home.html', context)