from abc import ABC,abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CashPaymentStrategy(PaymentStrategy):
    def pay(self,amount):
        print(f"${amount} paid via Cash")

class CardPaymentStrategy(PaymentStrategy):
    def pay(self,amount):
        print(f"${amount} paid via Card")

class Payment:
    def __init__(self,strategy):
        self.strategy=strategy

    def set_strategy(self,strategy):
        self.strategy=strategy

    def make_payment(self,amount):
        self.strategy.pay(amount)