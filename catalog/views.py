from django.shortcuts import render
from catalog.models import Book, BookInstance, Author, Genre

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    num_book_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_available_instance = BookInstance.objects.filter(status__exact='a').count()
    num_genre = Genre.objects.filter(name__icontains='fiction').count()
    num_books_with_the_in_title = Book.objects.filter(title__icontains='the').count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_book_instances': num_book_instances,
        'num_available_instance': num_available_instance,
        'title': 'Home',
        'num_genre': num_genre,
        'num_books_with_the_in_title': num_books_with_the_in_title,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
