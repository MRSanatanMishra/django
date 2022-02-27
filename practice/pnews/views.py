from django.shortcuts import render

# Create your views here.
from .models import *

def main_pageNews(request):
    data={'cat': Category.objects.all(),
            'news' : News.objects.all() }
    return render(request,'home.html',context=data)