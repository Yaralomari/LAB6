from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.view_one_book, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path("html5/links", views.html5_links, name="html5_links"),
    path("html5/links", views.html5_links, name="html5_links"),
    path("html5/text/formatting", views.html5_formatting, name="html5_formatting"),
    path("html5/listing", views.html5_listing, name="html5_listing"),
    path("html5/tables", views.html5_tables, name="html5_tables"),
    path('search', views.search, name='search'),
    
]