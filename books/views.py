from django.shortcuts import render
from django.views import generic
from .models import Book

# Create your views here.
class BooksList(generic.ListView):
    queryset = Book.objects.all()
    template_name = "books_list.html"
