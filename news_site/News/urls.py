from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<int:category_id>", views.category, name="category"),
    path("contact/", views.contact, name="contact"),
    path("view/<int:news_id>", views.view, name="view"),
    path("search/", views.search, name="search"),
]
