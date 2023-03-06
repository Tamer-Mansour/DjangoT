from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('logout/', logout, name='logout'),
    path('myaccount/<int:user_id>/', edit_profile, name='edit_profile'),
    path('quotes/', quotes, name='quotes'),
    path('user/<int:user_id>/', user_quotes, name='user_quotes'),
    path('delete_quote/<int:quote_id>/', delete_quote, name='delete_quote'),
    path('like/<int:quote_id>/', like_quote, name='like_quote'),
    path('unlike/<int:quote_id>/', unlike_quote, name='unlike_quote'),
]
