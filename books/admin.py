from django.contrib import admin
from .models import Book, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'slug', 'status', 'approved')
    search_fields = ['title', 'author']
    list_filter = ('status', 'created_on')
    summernote_fields = ('summary',)

    actions = ['mark_as_approved']

    def mark_as_approved(self, request, queryset):
        queryset.update(approved=True)
    mark_as_approved.short_description = "Approve selected books"


# Register your models here.
admin.site.register(Comment)