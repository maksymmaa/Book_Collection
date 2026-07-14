import json

from book_collection.config import FILE_NAME
from book_collection.models.book import Book

type Books = list[dict[str, str | int]]

def load_books() -> list[Book]:
    with open(FILE_NAME, encoding='utf-8') as file:
        data: Books = json.load(file)

    return [
        Book(
            book['title'],
            book['author'],
            book['year'],
            book['pages']
        )
        for book in data
    ]

def save_books(books: list[Book]) -> None:
    data: Books = [book.to_dict() for book in books]

    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def add_book(books: list[Book], title: str, author: str, year: int, pages: int) -> None:
    books.append(Book(title, author, year, pages))

def show_books(books: list[Book]) -> None:
    for book in books:
        print(book)

def find_longest_book(books: list[Book]) -> Book:
    return max(books)

def sort_books(books: list[Book]) -> list[Book]:
    return sorted(books)