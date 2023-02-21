from django.urls import path
from . import views

app_name = 'words'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_word', views.add_word, name='add_word'),
    path('clear', views.clear, name='clear'),
]
