from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.allWords, name = "getall"),
    path("<int:key>", views.singleWord, name = "getone"),
    path("", views.index, name = "index"),
]