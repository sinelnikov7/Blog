from django import forms

from api.models import Book, Genres


class BookForm(forms.ModelForm):

    genres = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple, queryset=Genres.objects.all(), label='Жанры')

    class Meta:
        model = Book
        fields = '__all__'

