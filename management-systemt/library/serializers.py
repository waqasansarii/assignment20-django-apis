from rest_framework import serializers
from . import models

class AuthorSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Authors
        fields = '__all__'


class GenresSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Genres
        fields = '__all__'


class BooksSerializer (serializers.ModelSerializer):
    author_name = serializers.CharField(source='author_id.name', read_only=True)
    genre_name = serializers.CharField(source='genre_id.name', read_only=True)
    class Meta:
        model = models.Books
        fields = ['title', 'published_date', 'author_name', 'genre_name', 'created_at']

        