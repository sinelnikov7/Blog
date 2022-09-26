from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from api.models import Book, Genres, Writer
from crud.forms import BookAddForm

def get_all_books(request):
    books = Book.objects.all().order_by('id')
    writers = Writer.objects.all()
    context = {
        'books': books,
        'writers': writers,
    }
    if request.method == "POST":
        name = request.POST.get("name")
        writer = int(request.POST.get("writer"))
        Book.objects.create(name=name, writer_id=writer)
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
    writers = Writer.objects.all()
    print(book.writer_id, 'qqqqqqq')
    context = {
        'book': book,
        'writers': writers,
    }
    if request.method == "POST":
        name = request.POST.get("name")
        writer = int(request.POST.get("writer"))
        book = Book.objects.get(id=pk)
        book.name = name
        book.writer_id = writer
        book.save()
        return redirect('crud:get_all_books')
    return render(request, 'change_book.html', context)

