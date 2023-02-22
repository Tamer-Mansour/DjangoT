from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    address = models.TextField()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    subject = models.CharField(max_length=100)
    address = models.TextField()


class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()


class Salary(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()


class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    date = models.DateField()
