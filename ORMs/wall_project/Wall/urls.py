from django.urls import path
from .views import wall, add_message, add_comment, delete_message

app_name = 'wall'

urlpatterns = [
    path('', wall, name='wall'),
    path('add_message/', add_message, name='add_message'),
    path('add_comment/<int:message_id>/', add_comment, name='add_comment'),
    path('delete_message/<int:message_id>/', delete_message, name='delete_message'),
]
