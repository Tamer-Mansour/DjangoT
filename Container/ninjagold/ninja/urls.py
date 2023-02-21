from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process_gold/', views.process_gold, name='process_gold'),
]
