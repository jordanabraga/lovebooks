from django.contrib import admin
from .models import Book, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'slug', 'status')
    search_fields = ['title', 'author']
    list_filter = ('status', 'created_on')
    summernote_fields = ('summary',)


# Register your models here.
admin.site.register(Comment)