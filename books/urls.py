from . import views
from django.urls import path

urlpatterns = [
    path('', views.BooksList.as_view(), name='home'),
]