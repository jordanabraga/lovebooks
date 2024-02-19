from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200, unique=False)
    slug = AutoSlugField(populate_from='title', always_update=True)
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="add_book"
    )
    summary = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.title} by {self.author}"