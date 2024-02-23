from . import views
from django.urls import path

urlpatterns = [
    path('', views.BooksList.as_view(), name='home'),
    path('creator_view/', views.add_book, name='creator_view'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'), 
]

