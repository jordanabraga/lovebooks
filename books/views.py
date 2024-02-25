from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book, Comment
from .forms import CommentForm, AddBook
from django.db.models import Q


# Create your views here.
class BooksList(generic.ListView):
    queryset = Book.objects.all().order_by("-created_on").filter(approved=True, status=1)
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
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.added_by = request.user
            comment.book = book
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "books/book_detail.html",
        {"book": book,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
         },
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Book.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.added_by == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = True
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
                messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Book.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.added_by == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))


#create view


def add_book(request):
    if request.method == 'POST':
        form = AddBook(request.POST, request.FILES)
        if form.is_valid():
            # Assign the current user to the added_by field before saving the form
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Book submitted and awaiting approval'
            )
            return redirect('creator_view')

    else:
        form = AddBook()
    return render(request, 'books/creator_view.html', {'form': form})


# Define function to search book
class SearchView(generic.ListView):
    model = Book
    template_name = 'books/index.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        ).order_by('title', 'author')
        
        # Check if queryset is empty
        if not queryset:
            messages.info(self.request, "No books found matching your search criteria. Try typing an author's name or a book title.")
        
        return queryset