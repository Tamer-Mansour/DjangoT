from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:user_id>/wall/', views.wall, name='wall'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name="register"),
    path('message/', views.message, name="message"),
    path('message/<int:message_id>/delete/',
         views.delete_message, name="delete_message"),
    path('comment/', views.comment, name="comment"),
    path('comment/<int:comment_id>/delete/',
         views.delete_comment, name="delete_comment"),
]
