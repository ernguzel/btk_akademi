from kutuphane_yonetimi.utils.log import Logger
from kutuphane_yonetimi.utils.penalties import PenaltyStrategy
from kutuphane_yonetimi.models.book import Book
from kutuphane_yonetimi.models.users import User


class LendingServices:
    def __init__(self, penalty_strategy: PenaltyStrategy):
        self.penalty_strategy = penalty_strategy
        self.logger = Logger()
    
    def lend(self, user: User , book: Book):
        if not book.is_available:
            self.logger.log("Kitap mevcut degil")
            return
        
        book.is_available = False
        self.logger.log(f"{user.name} kitabi aldi basligida {book.title}")

    def return_book(self, book: Book , days_late: int):
        book.is_available = True
        penalty = self.penalty_strategy.calculate(days_late)
        self.logger.log(f"kitap iade edildi cezasi da {penalty} tl")
        return penalty