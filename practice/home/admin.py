from django.contrib import admin
#from atexit import register
from .models import *

#admin.site.register(MovieRelease)
@admin.register(MovieRelease)
class MovieReleaseAdmin(admin.ModelAdmin):
    '''Admin View for MovieRelease'''

    list_display = ('title','studio','release_date',)
   
    ordering = ('release_date',)
