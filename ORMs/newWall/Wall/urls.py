from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('wall/', views.wall, name='wall'),
    path('message/', views.post_message, name='post_message'),
    path('comment/<int:msg_id>/', views.post_comment, name='post_comment'),
    path('logout/', views.logout, name='logout'),
]
