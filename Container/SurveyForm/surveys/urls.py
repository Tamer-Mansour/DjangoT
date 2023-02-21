from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey, name='survey'),
    path('process', views.process, name='process'),
    path('result', views.result, name='result'),
]
