import services.book_service as bs
import json

from models.book import Book

def main() -> None:
    try:
        books: list[Book] = bs.load_books()
    except (FileNotFoundError, json.JSONDecodeError):
        print('\nFile not found! Creating a new one...\n')
        books: list[Book] = []
        bs.save_books(books)

    print('BOOK COLLECTION'.center(70, '-'))
    print()

    while True:
        print('1. Add a book\n'
              '2. Show books\n'
              '3. Find longest book\n'
              '4. Sort books\n'
              '5. Compare books\n'
              'q. Exit\n')

        choice: str = input('Please enter something to choose a function: ').lower().strip()
        print()

        match choice:
            case '1':
                title: str = input('Enter the title: ')
                author: str = input('Enter the author: ')

                try:
                    year: int = int(input('Enter the year of the book: '))
                except ValueError:
                    print('\nYear should be entered as integer!\n')
                    continue

                try:
                    pages: int = int(input('Enter the number of pages: '))
                except ValueError:
                    print('\nPages should be entered as integer!\n')
                    continue

                print()

                bs.add_book(books, title, author, year, pages)

                bs.save_books(books)

                print('Book successfully added!')
                print()
            case '2':
                if not books:
                    print('There is no book yet!')
                    print()
                    continue

                bs.show_books(books)
            case '3':
                if not books:
                    print('There is no book yet!')
                    print()
                    continue

                print(f'Longest book:\n\n{bs.find_longest_book(books)}')
            case '4':
                if not books:
                    print('There is no book yet!')
                    print()
                    continue

                print('Sorted books:\n')

                sorted_books: list[Book] = bs.sort_books(books)

                bs.show_books(sorted_books)
            case '5':
                if not books:
                    print('There is no book yet!')
                    print()
                    continue

                try:
                    book1_index: int = int(input('Please enter index (0-n) of the first book to compare: '))
                except ValueError:
                    print('\nIndex should be entered as integer!\n')
                    continue

                try:
                    book2_index: int = int(input('Please enter index (0-n) of the second book to compare: '))
                except ValueError:
                    print('\nIndex should be entered as integer!\n')
                    continue

                try:
                    book1: Book = books[book1_index]
                except IndexError:
                    print('\nIndex is out of range!\n')
                    continue

                try:
                    book2: Book = books[book2_index]
                except IndexError:
                    print('\nIndex is out of range!\n')
                    continue

                print()

                print(f'Equals: {book1 == book2}')
                print()
            case 'q':
                print('Exiting the program...')
                break
            case _:
                print('Undefined value!')
                print()

if __name__ == '__main__':
    main()