from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path('api/users/', UserList.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
