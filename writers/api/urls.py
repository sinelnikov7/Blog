from django.urls import path, include

from rest_framework import routers

from .views import GetCities, GetGenres, GetWriters
from .viewsets import BookViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('genres/', GetGenres.as_view()),
    path('cities/', GetCities.as_view()),
    path('writers/', GetWriters.as_view()),
]
