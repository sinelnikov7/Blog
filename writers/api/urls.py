from django.urls import path

from .views import GetCities, GetGenres, GetWriters

urlpatterns = [
    path('genres/', GetGenres.as_view()),
    path('cities/', GetCities.as_view()),
    path('writers/', GetWriters.as_view()),
]
