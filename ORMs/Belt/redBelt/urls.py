from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('logout/', logout, name='logout'),
    path('myaccount/<int:user_id>/', edit_profile, name='edit_profile'),
]
