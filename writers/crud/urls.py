from django.urls import path, include

from .views import get_all_books, book_details, delete_book, ChangeBook

app_name = 'crud'

urlpatterns = [
    path('books/', get_all_books, name='get_all_books'),
    path('books/<int:pk>/', book_details, name='detail'),
    path('books/delete/<int:pk>', delete_book, name='delete_book'),
    path('books/change/<int:pk>', ChangeBook.as_view(), name='change_book',)
]
