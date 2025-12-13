class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def log(self, msg: str):
        print("[LOG]",msg)

class PricingStrategy:
    def calculate(self, base: float) ->float: ...

class NoDiscount(PricingStrategy):
    def calculate(self, base: float) -> float:
        return base
    
class StudentDiscount(PricingStrategy):
    def calculate(self, base: float) -> float:
        return base * 0.90

class BlackFridayDiscount(PricingStrategy):
    def calculate(self, base: float) -> float:
        return base * 0.50
    

class PaymentMethod:
    def pay(self, amount: float): ...

class CredictCardPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"kradi karti ile ödeme: {amount} yapildi")

class PayPalPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"pay pal ile ödeme: {amount} tl yapildi")

class PaymentFactory:
    @staticmethod
    def create(method: str) -> PaymentMethod:
        if method == "kart":
            return CredictCardPayment()
        if method == "paypal":
            return PayPalPayment()
        raise ValueError("desteklenmeyen odeme yontemi")
    
def process_order(price: float , method: str , strategy: PricingStrategy):
    log = Logger()

    final_price = strategy.calculate(price)
    log.log(f"hesaplanan fiyat: {final_price}")

    payment = PaymentFactory.create(method)

    payment.pay(final_price)
    log.log("ödeme tamamlandi")



process_order(100,"kart",StudentDiscount())
