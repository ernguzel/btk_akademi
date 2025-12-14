from kutuphane_yonetimi.utils.log import Logger
from kutuphane_yonetimi.models.book import Book

class BookService:
    def __init__(self):
        self.books: list[Book] = []
        self.logger = Logger()

    def add_book(self, book: Book):
        self.books.append(book)
        self.logger.log(f"Kitap eklendi kitabin basligi: {book.title}")

    def find_book(self, title: str) -> Book | None:
        return next((b for b in self.books if b.title == title),None)
    
    