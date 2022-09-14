from rest_framework import serializers

from .models import City, Genres, Writer


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genres
        depth = 0
        fields = '__all__'


class СitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        depth = 0
        fields = '__all__'


class WritersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Writer
        depth = 1
        fields = '__all__'
