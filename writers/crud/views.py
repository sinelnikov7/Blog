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
        book = Book.objects.create(name=name, writer_id=writer)
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


class ChangeBook(UpdateView):
    model = Book
    template_name = 'change_book.html'
    form_class = BookAddForm
    success_url = reverse_lazy('crud:get_all_books')
# Create your views here.
