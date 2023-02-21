from django .urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_book', views.create_book),
    path('books/<int:book_id>', views.view_book),
    path('books/<int:book_id>/update', views.update_book),
    path('books/<int:book_id>/delete', views.delete_book),
    path('add_author_to_the_book/<int:book_id>', views.add_author_to_the_book),
    path('authors', views.authors),
    path('create_author', views.create_author),
    path('authors/<int:author_id>', views.view_author),
    path('authors/<int:author_id>/update', views.update_author),
    path('authors/<int:author_id>/delete', views.delete_author),
    path('add_book_to_the_author/<int:author_id>', views.add_book_to_the_author)
]
