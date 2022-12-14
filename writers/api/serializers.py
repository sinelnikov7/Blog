from rest_framework import serializers

from .models import City, Genres, Writer, Book


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genres
        depth = 0
        fields = '__all__'


class –°itiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        depth = 0
        fields = '__all__'


class WritersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Writer
        depth = 1
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        depth = 1
        fields = '__all__'
