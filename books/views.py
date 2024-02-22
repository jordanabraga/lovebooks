from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book

# Create your views here.
class BooksList(generic.ListView):
    queryset = Book.objects.all().order_by("-created_on")
    template_name = "books/index.html"
    paginate_by = 3

def book_detail(request, slug):
    """
    Display an individual :model:`books.Book`.

    **Context**

    ``book``
        An instance of :model:`books.Book`.

    **Template:**

    :template:`book/book_detail.html`
    """

    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)
    comments = book.comments.all().order_by("-created_on")
    comment_count = book.comments.filter(approved=True).count()

    return render(
        request,
        "books/book_detail.html",
        {"book": book,
         "comments": comments,
         "comment_count": comment_count,},
    )