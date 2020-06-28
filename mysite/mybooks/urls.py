from django.contrib import admin
from django.urls import include, path
from . import views
#from .views import StatView

# list these in same order as views for elegance!
urlpatterns = [
     path(
         "",
         views.index,
         name="index"
         ),

     path(
         "success/",
         views.success,
         name="success"
         ),

     path(
         "mybooks/add/",
         views.create_book,
         name="create_book"
         ),

     path(
         "mybooks/<int:pk>/",
         views.book_detail,
         name="book_detail"
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
         "contact-donate/",
         views.contact_donate,
         name="contact-donate"
         ),

     path(
         "terms-conditions/",
         views.terms_conditions,
         name="terms-conditions"
         ),

    path(
        "mybooks/<int:pk>/stats",
        views.stats,
        name="stats"
        ),

    #path(
    #    "mybooks/<int:pk>/stats",
    #    views.words_remaining,
    #    name="words_remaining"
    #    ),
]
