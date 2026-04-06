from django.shortcuts import render
from .models import Book

def index(request):
    return render(request, "bookmodule/index.html")


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def view_one_book(request, bookId):

    books = {
        1: {
            "title": "Internet & World Wide Web How to Program",
            "author": "author name",
            "image": "book1.jpg",
            "description": "provides a clear introduction to web programming."
        },
        2: {
            "title": "C++ How to Program",
            "author": "author name",
            "image": "book2.jpg",
            "description": "A comprehensive guide to C++ programming."
        },
        3: {
            "title": "Images in Another Folder",
            "author": "author name",
            "image": "book3.jpg",
            "description": "Example book demonstrating images."
        }
    }

    book = books.get(bookId)

    return render(request, "bookmodule/one_book.html", {
        "book": book
    })


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def html5_links(request):
    return render(request, "bookmodule/html5/links.html")


def html5_formatting(request):
    return render(request, "bookmodule/html5/formatting.html")


def html5_listing(request):
    return render(request, "bookmodule/html5/listing.html")


def html5_tables(request):
    return render(request, "bookmodule/html5/tables.html")


def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]


def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')
def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False)\
        .filter(title__icontains='and')\
        .filter(edition__gte=2)\
        .exclude(price__lte=100)[0:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')