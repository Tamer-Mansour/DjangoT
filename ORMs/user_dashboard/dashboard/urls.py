from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('users/register/', views.register, name='register_user'),
    path('users/login/', views.login, name='login_user'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/new/', views.users_new, name='new_user'),
    path('users/show/<int:id>/', views.users_homepage, name='show_user'),
    path('users/edit/<int:id>/', views.edit, name='edit_user'),
    path('users/edit_users/', views.edit_users, name='edit_users'),
    path('users/delete/<int:id>/', views.delete, name='delete_user'),
    path('logout/', views.logout, name='logout'),
]
