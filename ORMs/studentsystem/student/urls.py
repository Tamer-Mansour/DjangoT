from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('invoices/', views.invoices, name='invoices'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('add_invoice/', views.add_invoice, name='add_invoice'),
]
