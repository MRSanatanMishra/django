from django.contrib import admin
from .models import *

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','created_on')
    ordering=('-created_on',)    


@admin.register(Biscuit)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name','flavour','price','created_on')
    ordering=('-created_on',)    
