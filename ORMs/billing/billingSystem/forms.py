from django import forms
from .models import Student, Teacher, Fee, Salary, Invoice


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'class_name', 'parent_name', 'address']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'age', 'subject', 'address']


class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['student', 'amount', 'date']


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['teacher', 'amount', 'date']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['student', 'teacher', 'fee', 'salary', 'total_amount', 'date']
