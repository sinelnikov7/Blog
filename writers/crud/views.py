from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from api.models import Book, Genres, Writer
from .forms import BookForm

def get_all_books(request):
    books = Book.objects.all().order_by('id')
    writers = Writer.objects.all()
    genres = Genres.objects.all()
    forms = BookForm()
    context = {
        'books': books,
        'writers': writers,
        'genres': genres,
        'forms': forms,
    }
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('crud:get_all_books')
    return render(request, 'get_all_books.html', context)

def book_details(request, pk):
    book = Book.objects.get(id=pk)
    context = {
        'book': book,
    }
    return render(request, 'book_details.html', context)

def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('crud:get_all_books')

def change_book(request, pk):
    book = Book.objects.get(id=pk)
    forms = BookForm(instance=book)
    context = {
        'forms': forms,
    }
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('crud:get_all_books')
    return render(request, 'change_book.html', context)

