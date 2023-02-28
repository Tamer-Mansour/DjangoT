from django.urls import path
from .views import register, login, home, logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout, name='logout'),
]
