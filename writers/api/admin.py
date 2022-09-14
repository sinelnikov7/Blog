from django.contrib import admin

from .models import City, Genres, Writer

admin.site.register(Genres)
admin.site.register(City)
admin.site.register(Writer)
# Register your models here.
