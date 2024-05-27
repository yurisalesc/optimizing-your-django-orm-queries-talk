from django.db import connection

from .helpers import debug_queries
from .models import Author, Book, Review


@debug_queries()
def get_id_from_all_book_authors():
    books = Book.objects.all()
    for book in books:
        print(book.author.id)


@debug_queries()
def get_id_from_all_book_authors_good():
    books = Book.objects.all()
    for book in books:
        print(book.author_id)


@debug_queries()
def count_authors_with_len():
    print(len(Author.objects.all()))


@debug_queries()
def count_authors_with_count():
    print(Author.objects.count())


@debug_queries()
def get_review_rating():
    review = Review.objects.values_list("id", "rating")[:5]
    print(review)

    review = Review.objects.values("id", "rating")[:5]
    print(review)

    review = Review.objects.only("id", "rating")[:5]
    print(review)

    print(connection.queries)


@debug_queries()
def get_review_rating_bad():
    review = Review.objects.all()[:5]
    print(review)
    print(connection.queries)


@debug_queries()
def create_authors():
    for i in range(20):
        Author.objects.create(name=f"Fulano {i}")


@debug_queries()
def create_authors_with_bulk_create():
    authors = (Author(name=f"Beltrano {i}") for i in range(20))
    Author.objects.bulk_create(authors)


authors = Author.objects.all()[:20]


@debug_queries()
def update_authors_individually():
    for i, author in enumerate(authors):
        author.name = f'Updated Author {i + 1}'
        author.save()


@debug_queries()
def bulk_update_20_authors():
    for i, author in enumerate(authors):
        author.name = f'Bulk Updated Author {i + 1}'

    Author.objects.bulk_update(authors, ['name'])


@debug_queries()
def list_books_with_authors():
    books = Book.objects.all()
    for book in books:
        print(f"{book.title} - {book.author.name}")


@debug_queries()
def list_books_with_authors_with_select_related():
    books = Book.objects.select_related("author")
    for book in books:
        print(f"{book.title} - {book.author.name}")


@debug_queries()
def list_categories_from_all_books():
    books = Book.objects.all()
    for book in books:
        print(f"{book.title}")
        for category in book.categories.all():
            print(f"---->{category.name}")


@debug_queries()
def list_categories_from_all_books_with_prefetch_related():
    books = Book.objects.all().prefetch_related("categories")
    for book in books:
        print(f"{book.title}")
        for category in book.categories.all():
            print(f"---->{category.name}")
