from django.db import models

class Authors(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Genres(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Books(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField(null=True)
    author_id = models.ForeignKey('Authors', on_delete= models.CASCADE)
    genre_id = models.ForeignKey('Genres', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    