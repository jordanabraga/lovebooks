from .models import Comment, Book
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'featured_image', 'summary', 'status',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the book title', 'maxlength': 100}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter the author name', 'maxlength': 100}),
            'summary': forms.Textarea(attrs={'placeholder': 'Enter the book summary', 'maxlength': 100}),
        }