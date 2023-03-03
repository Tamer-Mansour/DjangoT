from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('verify_email/str:verification_code/', verify_email, name='verify_email'),
    path('profile/', profile, name='profile'),
    path('user_list/', user_list, name='user_list'),
    path('user_edit/<int:pk>/', user_edit, name='user_edit'),
    path('user_delete/<int:pk>/', user_delete, name='user_delete'),
    path('create_post/', create_post, name='create_post'),
    path('', posts_list, name='posts_list'),
    path('post_detail/int:pk/', post_detail, name='post_detail'),
]
