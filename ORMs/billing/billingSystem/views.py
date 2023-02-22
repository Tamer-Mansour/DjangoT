from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *


# Student views

def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student_list.html', context)


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'student_detail.html', context)


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    context = {'form': form}
    return render(request, 'student_form.html', context)


def student_update(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    context = {'form': form}
    return render(request, 'student_form.html', context)


def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    context = {'student': student}
    return render(request, 'student_delete.html', context)


# Teacher views

def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teacher_list.html', context)


def teacher_detail(request, pk):
    teacher = Teacher.objects.get(id=pk)
    context = {'teacher': teacher}
    return render(request, 'teacher_detail.html', context)


def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    context = {'form': form}
    return render(request, 'teacher_form.html', context)


def teacher_update(request, pk):
    teacher = Teacher.objects.get(id=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    context = {'form': form}
    return render(request, 'teacher_form.html', context)


def teacher_delete(request, pk):
    teacher = Teacher.objects.get(id=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    context = {'teacher': teacher}
    return render(request, 'teacher_delete.html', context)


def fee_list(request):
    fees = Fee.objects.all()
    context = {'fees': fees}
    return render(request, 'fee_list.html', context)


def fee_detail(request, pk):
    fee = Fee.objects.get(id=pk)
    context = {'fee': fee}
    return render(request, 'fee_detail.html', context)


def fee_create(request):
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fee_list')
    else:
        form = FeeForm()
    context = {'form': form}
    return render(request, 'fee_form.html', context)


def fee_update(request, pk):
    fee = Fee.objects.get(id=pk)
    if request.method == 'POST':
        form = FeeForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            return redirect('fee_list')
    else:
        form = FeeForm(instance=fee)
    context = {'form': form}
    return render(request, 'fee_form.html', context)


def fee_delete(request, pk):
    fee = Fee.objects.get(id=pk)
    fee.delete()
    return redirect('fee_list')

# Salary views


def salary_list(request):
    salaries = Salary.objects.all()
    context = {'salaries': salaries}
    return render(request, 'salary_list.html', context)


def salary_detail(request, pk):
    salary = Salary.objects.get(id=pk)
    context = {'salary': salary}
    return render(request, 'salary_detail.html', context)


def salary_create(request):
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryForm()
    context = {'form': form}
    return render(request, 'salary_form.html', context)


def salary_update(request, pk):
    salary = Salary.objects.get(id=pk)
    if request.method == 'POST':
        form = SalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('salary_detail', pk=salary.id)
    else:
        form = SalaryForm(instance=salary)
    context = {'form': form}
    return render(request, 'salary_form.html', context)


def salary_delete(request, pk):
    salary = Salary.objects.get(id=pk)
    if request.method == 'POST':
        salary.delete()
        return redirect('salary_list')
    context = {'salary': salary}
    return render(request, 'salary_delete.html', context)


# Invoice views

def invoice_list(request):
    invoices = Invoice.objects.all()
    context = {'invoices': invoices}
    return render(request, 'invoice_list.html', context)


def invoice_detail(request, pk):
    invoice = Invoice.objects.get(id=pk)
    context = {'invoice': invoice}
    return render(request, 'invoice_detail.html', context)


def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    context = {'form': form}
    return render(request, 'invoice_form.html', context)


def invoice_update(request, pk):
    invoice = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_detail', pk=invoice.id)
    else:
        form = InvoiceForm(instance=invoice)
    context = {'form': form}
    return render(request, 'invoice_form.html', context)


def invoice_delete(request, pk):
    invoice = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        invoice.delete()
        return redirect('invoice_list')
    context = {'invoice': invoice}
    return render(request, 'invoice_delete.html', context)
