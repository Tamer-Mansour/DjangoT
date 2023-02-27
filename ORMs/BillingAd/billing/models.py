from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('manager', 'manager'),
        ('accountant', 'accountant'),
        ('teacher', 'teacher'),
        ('student', 'student'),
    )
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)
    forth_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)

class Accountant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='accountant')
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    parent_phone_number = models.CharField(max_length=15)
    whatsapp_mother_number = models.CharField(max_length=15)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.CharField(max_length=50)
    class_value = models.CharField(max_length=2)

class Invoice(models.Model):
    INVOICE_CHOICES = (
        ('student', 'student'),
        ('teacher', 'teacher'),
    )
    type = models.CharField(choices=INVOICE_CHOICES, max_length=10)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_invoices', null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_invoices', null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
