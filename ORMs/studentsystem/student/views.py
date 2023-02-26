from django.shortcuts import render, redirect
from .models import Student, Teacher, Invoice

def students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def invoices(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices.html', {'invoices': invoices})

def add_student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        enrollment_date = request.POST['enrollment_date']
        student = Student(first_name=first_name, last_name=last_name, enrollment_date=enrollment_date)
        student.save()
        return redirect('students')
    return render(request, 'add_student.html')

def add_teacher(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        hire_date = request.POST['hire_date']
        yearly_salary = request.POST['yearly_salary']
        teacher = Teacher(first_name=first_name, last_name=last_name, hire_date=hire_date, yearly_salary=yearly_salary)
        teacher.save()
        return redirect('teachers')
    return render(request, 'add_teacher.html')

def add_invoice(request):
    if request.method == 'POST':
        student = Student.objects.get(id=request.POST['student'])
        teacher = Teacher.objects.get(id=request.POST['teacher'])
        amount = request.POST['amount']
        invoice_date = request.POST['invoice_date']
        invoice = Invoice(student=student, teacher=teacher, amount=amount, invoice_date=invoice_date)
        invoice.save()
        return redirect('invoices')
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'add_invoice.html', {'students': students, 'teachers': teachers})
