from django.urls import path

from .views import main_pageNews


urlpatterns = [
    path('', main_pageNews,name='pnewsHome'),
]