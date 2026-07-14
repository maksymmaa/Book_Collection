import json

from book_collection.config import FILE_NAME
from book_collection.models.book import Book

def load_books():
    with open(FILE_NAME, encoding='utf-8') as file:
        data = json.load(file)

    return [
        Book(
            book['title'],
            book['author'],
            book['year'],
            book['pages']
        )
        for book in data
    ]

def save_books(books):
    data = [book.to_dict() for book in books]

    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def add_book(books, title, author, year, pages):
    books.append(Book(title, author, year, pages))

def show_books(books):
    for book in books:
        print(book)

def find_longest_book(books):
    return max(books)

def sort_books(books):
    return sorted(books)