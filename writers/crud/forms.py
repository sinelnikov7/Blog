from django import forms

from api.models import Book, Genres, Writer


class BookForm(forms.Form):

    name = forms.CharField(max_length=100, label='Название')
    writer = forms.ModelChoiceField(widget=forms.Select, queryset=Writer.objects.all(), label='Писатель')
    genres = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple, queryset=Genres.objects.all(), label='Жанры')
