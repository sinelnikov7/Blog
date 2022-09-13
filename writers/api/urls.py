from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('getgenres/', GetGenres.as_view()),
    path('getcitys/', GetCitys.as_view()),
    path('getwriters/', GetWriters.as_view()),

]
