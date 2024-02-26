from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200, unique=False)
    slug = AutoSlugField(populate_from='title', always_update=True)
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="add_book"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    summary = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} by {self.author}"


class Comment(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments_user"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.added_by}" \
            f" Approved: {self.approved}"
