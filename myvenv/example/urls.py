from django.contrib import admin
from django.urls import path, include
from .views import HelloAPI, bookAPI, booksAPI

urlpatterns = [
    path('hello/',HelloAPI.as_view()),
    path('cbv/books/', booksAPI.as_view()),
    path('cbv/book/<int:bid>', bookAPI.as_view())
]