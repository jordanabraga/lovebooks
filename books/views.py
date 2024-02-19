from django.shortcuts import render
from django.views import generic
from .models import Book

# Create your views here.
class BooksList(generic.ListView):
    queryset = Book.objects.all().order_by("-created_on")
    template_name = "books_list.html"
