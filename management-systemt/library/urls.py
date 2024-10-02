from django.urls import path
from .views import get_authors,get_update_authors,get_genres,get_update_genres,get_books,get_update_books

urlpatterns =[
    path('authors/',get_authors),
    path('authors/<id>',get_update_authors),
    path('genres/',get_genres),
    path('genres/<id>',get_update_genres),
    path('books/',get_books),
    path('books/<id>',get_update_books),
]