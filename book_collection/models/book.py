class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        return (f'{self.title}\n'
                f'Author: {self.author}\n'
                f'Year: {self.year}\n'
                f'Pages: {self.pages}\n')

    def __repr__(self):
        return f'Book(title=\'{self.title}\', author=\'{self.author}\', year={self.year}, pages={self.pages})'

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.pages < other.pages

    def __contains__(self, item):
        return True if item in self.title else False

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'pages': self.pages
        }