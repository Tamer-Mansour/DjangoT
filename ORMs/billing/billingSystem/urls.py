from django.urls import path
from .views import (
    student_list,
    student_detail,
    student_create,
    student_update,
    student_delete,
    teacher_list,
    teacher_detail,
    teacher_create,
    teacher_update,
    teacher_delete,
    fee_list,
    fee_detail,
    fee_create,
    fee_update,
    fee_delete,
    salary_list,
    salary_detail,
    salary_create,
    salary_update,
    salary_delete,
    invoice_list,
    invoice_detail,
    invoice_create,
    invoice_update,
    invoice_delete,
)

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/create/', student_create, name='student_create'),
    path('students/<int:pk>/', student_detail, name='student_detail'),
    path('students/<int:pk>/update/', student_update, name='student_update'),
    path('students/<int:pk>/delete/', student_delete, name='student_delete'),

    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/create/', teacher_create, name='teacher_create'),
    path('teachers/<int:pk>/', teacher_detail, name='teacher_detail'),
    path('teachers/<int:pk>/update/', teacher_update, name='teacher_update'),
    path('teachers/<int:pk>/delete/', teacher_delete, name='teacher_delete'),

    path('fees/', fee_list, name='fee_list'),
    path('fees/create/', fee_create, name='fee_create'),
    path('fees/<int:pk>/', fee_detail, name='fee_detail'),
    path('fees/<int:pk>/update/', fee_update, name='fee_update'),
    path('fees/<int:pk>/delete/', fee_delete, name='fee_delete'),

    path('salaries/', salary_list, name='salary_list'),
    path('salaries/create/', salary_create, name='salary_create'),
    path('salaries/<int:pk>/', salary_detail, name='salary_detail'),
    path('salaries/<int:pk>/update/', salary_update, name='salary_update'),
    path('salaries/<int:pk>/delete/', salary_delete, name='salary_delete'),

    path('invoices/', invoice_list, name='invoice_list'),
    path('invoices/create/', invoice_create, name='invoice_create'),
    path('invoices/<int:pk>/', invoice_detail, name='invoice_detail'),
    path('invoices/<int:pk>/update/', invoice_update, name='invoice_update'),
    path('invoices/<int:pk>/delete/', invoice_delete, name='invoice_delete'),
]