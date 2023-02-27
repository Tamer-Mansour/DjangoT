from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User, Accountant, Teacher, Student, Invoice


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('billing:student_invoices')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'billing/login.html')


def logout(request):
    logout(request)
    return redirect('billing:login')


def student_invoices(request):
    invoices = Invoice.objects.filter(type='student')
    return render(request, 'billing/student_invoices.html', {'invoices': invoices})


def student_invoice(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    return render(request, 'billing/student_invoice.html', {'invoice': invoice})


def create_student_invoice(request):
    if request.method == 'POST':
        student = Student.objects.get(id=request.POST['student'])
        invoice = Invoice(type='student', student=student,
                          amount=request.POST['amount'], description=request.POST['description'])
        invoice.save()
        student.money -= invoice.amount
        student.save()
        return redirect('billing:student_invoices')
    students = Student.objects.all()
    return render(request, 'billing/create_student_invoice.html', {'students': students})


def update_student_invoice(request, invoice_id):
    if request.method == 'POST':
        invoice = Invoice.objects.get(id=invoice_id)
        student = invoice.student
        student.money += invoice.amount
        student.save()
        invoice.amount = request.POST['amount']
        invoice.description = request.POST['description']
        invoice.save()
        student.money -= invoice.amount
        student.save()
        return redirect('billing:student_invoices')
    invoice = Invoice.objects.get(id=invoice_id)
    return render(request, 'billing/update_student_invoice.html', {'invoice': invoice})


def delete_student_invoice(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    invoice.delete()
    return redirect('billing:student_invoices')


def teacher_invoices(request):
    invoices = Invoice.objects.filter(type='teacher')
    return render(request, 'billing/teacher_invoices.html', {'invoices': invoices})


def teacher_invoice(request):
    invoice = Invoice.objects.get(id=invoice_id)
    return render(request, 'billing/teacher_invoice.html', {'invoice': invoice})


def create_teacher_invoice(request):
    if request.method == 'POST':
        teacher = Teacher.objects.get(id=request.POST['teacher'])
        invoice = Invoice(type='teacher', teacher=teacher,
                          amount=request.POST['amount'], description=request.POST['description'])
        invoice.save()
        teacher.salary += invoice.amount
        teacher.save()
        return redirect('billing:teacher_invoices')
    teachers = Teacher.objects.all()
    return render(request, 'billing/create_teacher_invoice.html', {'teachers': teachers})


def update_teacher_invoice(request, invoice_id):
    if request.method == 'POST':
        invoice = Invoice.objects.get(id=invoice_id)
        teacher = invoice.teacher
        teacher.salary -= invoice.amount
        teacher.save()
        invoice.amount = request.POST['amount']
        invoice.description = request.POST['description']
        invoice.save()
        teacher.salary += invoice.amount
        teacher.save()
        return redirect('billing:teacher_invoices')
    invoice = Invoice.objects.get(id=invoice_id)
    return render(request, 'billing/update_teacher_invoice.html', {'invoice': invoice})


def delete_teacher_invoice(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    invoice.delete()
    return redirect('billing:teacher_invoices')


def manage_users(request):
    users = User.objects.all()
    return render(request, 'billing/manage_users.html', {'users': users})


def create_user(request):
    if request.method == 'POST':
        user = User(first_name=request.POST['first_name'], second_name=request.POST['second_name'],
                    third_name=request.POST['third_name'], forth_name=request.POST['forth_name'],
                    email=request.POST['email'], password=request.POST['password'],
                    date_of_birth=request.POST['date_of_birth'], role=request.POST['role'])
        user.save()
        if request.POST['role'] == 'accountant':
            accountant = Accountant(user=user, salary=request.POST['salary'])
            accountant.save()
        elif request.POST['role'] == 'teacher':
            teacher = Teacher(user=user, salary=request.POST['salary'])
            teacher.save()
        elif request.POST['role'] == 'student':
            student = Student(user=user, parent_phone_number=request.POST['parent_phone_number'],
                              whatsapp_mother_number=request.POST['whatsapp_mother_number'],
                              money=request.POST['money'], area=request.POST['area'], class_value=request.POST['class_value'])
            student.save()
        return redirect('billing:manage_users')
    return render(request, 'billing/create_user.html')


def update_user(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.first_name = request.POST['first_name']
        user.second_name = request.POST['second_name']
        user.third_name = request.POST['third_name']
        user.forth_name = request.POST['forth_name']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.date_of_birth = request.POST['date_of_birth']
        user.role = request.POST['role']
        user.save()
        if user.role == 'accountant':
            accountant = Accountant.objects.get(user=user)
            accountant.salary = request.POST['salary']
            accountant.save()
        elif user.role == 'teacher':
            teacher = Teacher.objects.get(user=user)
            teacher.salary = request.POST['salary']
            teacher.save()
        elif user.role == 'student':
            student = Student.objects.get(user=user)
            student.parent_phone_number = request.POST['parent_phone_number']
            student.whatsapp_mother_number = request.POST['whatsapp_mother_number']
            student.money = request.POST['money']
            student.area = request.POST['area']
            student.class_value = request.POST['class_value']
            student.save()
        return redirect('billing:manage_users')
    user = User.objects.get(id=user_id)
    return render(request, 'billing/update_user.html', {'user': user})


def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('billing:manage_users')
