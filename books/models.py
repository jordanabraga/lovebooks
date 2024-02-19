from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    slug = models.SlugField(max_length=200, unique=True)
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="add_book"
    )
    summary = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)