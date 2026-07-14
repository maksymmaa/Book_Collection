type BookDict = dict[str, str | int]

class Book:
    def __init__(self, title: str, author: str, year: int, pages: int) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self) -> str:
        return (f'{self.title}\n'
                f'Author: {self.author}\n'
                f'Year: {self.year}\n'
                f'Pages: {self.pages}\n')

    def __repr__(self) -> str:
        return (f'Book('
                f'title={self.title!r}, '
                f'author={self.author!r}, '
                f'year={self.year}, '
                f'pages={self.pages})')

    def __len__(self) -> int:
        return self.pages

    def __eq__(self, other) -> bool:
        return self.title == other.title and self.author == other.author

    def __lt__(self, other) -> bool:
        return self.pages < other.pages

    def __contains__(self, item) -> bool:
        return True if item in self.title else False

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        self.__title = value

    @title.deleter
    def title(self) -> None:
        print('Deleting title attribute...')
        print()
        del self.__title

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, value: str) -> None:
        self.__author = value

    @author.deleter
    def author(self) -> None:
        print('Deleting author attribute...')
        print()
        del self.__author

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, value: int) -> None:
        self.__year = value

    @year.deleter
    def year(self) -> None:
        print('Deleting year attribute...')
        print()
        del self.__year

    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, value: int) -> None:
        self.__pages = value

    @pages.deleter
    def pages(self) -> None:
        print('Deleting pages attribute...')
        print()
        del self.__pages

    def to_dict(self) -> BookDict:
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'pages': self.pages
        }