from django.shortcuts import render
from .models import *
# Create your views here.
def bakery_menu(request):
    ctx={'cakes':Cake.objects.all(),
        'biscuits':Biscuit.objects.all()}

    return render(request,'bakeryMenu.html',context=ctx)