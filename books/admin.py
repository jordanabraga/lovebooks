from django.contrib import admin
from .models import Book, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'slug', 'status', 'approved')
    search_fields = ['title', 'author', 'approved']
    list_filter = ('status', 'created_on', 'approved')
    summernote_fields = ('summary')

    actions = ['mark_as_approved']
    

    def mark_as_approved(self, request, queryset):
        queryset.update(approved=True)
    mark_as_approved.short_description = "Approve selected books"


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('book','added_by', 'body', 'approved')
    search_fields = ('approved', 'created_on', 'book')
    actions = ['mark_as_approved']

    def mark_as_approved(self, request, queryset):
        queryset.update(approved=True)
    mark_as_approved.short_description = "Approve selected books"

