from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
     path(
         "",
         views.index,
         name="index"
         ),

     path(
         "mybooks/",
         views.book_list,
         name="book_list"
         ),

     path(
         "mybooks/<int:pk>/",
         views.book_detail,
         name="book_detail"
         ),

     path(
         "mybooks/<int:pk>/stats",
         views.stats,
         name="stats"
         ),

     path(
         "mybooks/add/",
         views.create_book,
         name="create_book"
         ),

     path(
         "mybooks/<int:pk>/update/",
         views.update_book,
         name="update"
         ),

     path(
         "mybooks/<pk>/delete/",
         views.delete_book,
         name="delete"
         ),

     path(
         "about/",
         views.about,
         name="about"
         ),

     path(
         "contact/",
         views.contact,
         name="contact"
         ),

     path(
         "terms-conditions/",
         views.terms_conditions,
         name="terms-conditions"
         ),
]
