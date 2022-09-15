from django.contrib import admin

from .models import City, Genres, Writer, Book

admin.site.register(Genres)
admin.site.register(City)
admin.site.register(Writer)
admin.site.register(Book)
# Register your models here.
