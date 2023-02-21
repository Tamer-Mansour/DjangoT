from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, "index.html", context)


def create_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc']
        )
        return redirect('/')
    return redirect('/')


def view_book(request, book_id):
    context = {
        'one_book': Book.objects.get(id=book_id),
        'select_authors': []
    }

    for author in Author.objects.all():
        context['select_authors'].append(author)
    return render(request, 'book.html', context)


def add_author_to_the_book(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author'])
    author.books.add(book)
    return redirect(f'/books/{book_id}')


def authors(request):
    context = {
        'all_authers': Author.objects.all()
    }
    print('***********', context)
    return render(request, 'author.html', context)


def create_author(request):
    if request.method == 'POST':
        Author.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            notes=request.POST['notes']
        )
        return redirect('/authors')
    return redirect('/authors')


def view_author(request, author_id):
    context = {
        'one_author': Author.objects.get(id=author_id),
        'select_books': Book.objects.exclude(id=author_id)
    }
    return render(request, 'one_author.html', context)


def add_book_to_the_author(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=request.POST['book'])
    author.books.add(book)
    return redirect(f"/authors/{author_id}")


def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    author.delete()
    return redirect('/authors')


def update_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        author.first_name = request.POST['first_name']
        author.last_name = request.POST['last_name']
        author.notes = request.POST['notes']
        author.save()
        return redirect(f'/authors/{author_id}')
    context = {
        'one_author': author
    }
    return render(request, 'update_author.html', context)


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/')


def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.save()
        return redirect(f'/books/{book_id}')
    context = {
        'one_book': book
    }
    return render(request, 'update_book.html', context)
