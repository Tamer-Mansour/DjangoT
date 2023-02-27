from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('student_invoices/', views.student_invoices, name='student_invoices'),
    path('student_invoice/<int:invoice_id>/',
         views.student_invoice, name='student_invoice'),
    path('create_student_invoice/', views.create_student_invoice,
         name='create_student_invoice'),
    path('update_student_invoice/<int:invoice_id>/',
         views.update_student_invoice, name='update_student_invoice'),
    path('delete_student_invoice/<int:invoice_id>/',
         views.delete_student_invoice, name='delete_student_invoice'),
    path('teacher_invoices/', views.teacher_invoices, name='teacher_invoices'),
    path('teacher_invoice/<int:invoice_id>/',
         views.teacher_invoice, name='teacher_invoice'),
    path('create_teacher_invoice/', views.create_teacher_invoice,
         name='create_teacher_invoice'),
    path('update_teacher_invoice/<int:invoice_id>/',
         views.update_teacher_invoice, name='update_teacher_invoice'),
    path('delete_teacher_invoice/<int:invoice_id>/',
         views.delete_teacher_invoice, name='delete_teacher_invoice'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('create_user/', views.create_user, name='create_user'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]
