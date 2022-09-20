from django import forms

from api.models import Book


class BookAddForm(forms.ModelForm):

    class Meta:

        model = Book
        fields = '__all__'
