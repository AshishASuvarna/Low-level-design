from datetime import datetime
import uuid
from abc import ABC,abstractmethod
from Currency import Currency
from Conversion import Conversion
from Transaction import Transaction
from TransactionStatus import TransactionStatus

class PaymentMethod(ABC):
    def __init__(self,id,currency):
        self.id=id
        self.currency=currency

    @abstractmethod
    def pay(self,amount,sender_acc,receiver_acc):
        pass

class BankTransfer(PaymentMethod):
    def pay(self,amount,sender_acc,receiver_acc):
        sender_currency = sender_acc.get_currency()
        receiver_currency = receiver_acc.get_currency()

        transaction = Transaction(str(uuid.uuid4()), datetime.now(), amount, sender_currency,sender_acc.get_acc_number(), receiver_acc.get_acc_number(), TransactionStatus.PENDING)
        if sender_acc.get_balance() < amount:
            transaction.set_status(TransactionStatus.FAILED)
            print("Transaction failed: Insufficient balance in sender account.")
            return transaction

        try:
            if sender_currency != receiver_currency:
                converted_amount = Conversion.convert(amount, sender_currency, receiver_currency)
            else:
                converted_amount = amount

            sender_acc.withdraw(amount)
            receiver_acc.deposit(converted_amount)

            print(f"{amount} {sender_currency.name} transferred to {receiver_acc.get_acc_number()} "
                f"({converted_amount:.2f} {receiver_currency.name}) via Bank transfer")

            transaction.set_status(TransactionStatus.SUCCESS)

        except Exception as e:
            transaction.set_status(TransactionStatus.FAILED)
            print(f"Transaction failed: {e}")
            return transaction
        return transaction


class CreditCard(PaymentMethod):
    def pay(self, amount, sender_acc, receiver_acc):
        sender_currency = sender_acc.get_currency()
        receiver_currency = receiver_acc.get_currency()

        transaction = Transaction(str(uuid.uuid4()), datetime.now(), amount, sender_currency,sender_acc.get_acc_number(), receiver_acc.get_acc_number(), TransactionStatus.PENDING)
        if sender_acc.get_balance() < amount:
            transaction.set_status(TransactionStatus.FAILED)
            print("Transaction failed: Insufficient balance in sender account.")
            return transaction

        try:
            if sender_currency != receiver_currency:
                converted_amount = Conversion.convert(amount, sender_currency, receiver_currency)
            else:
                converted_amount = amount

            sender_acc.withdraw(amount)
            receiver_acc.deposit(converted_amount)

            print(f"{amount} {sender_currency.name} transferred to {receiver_acc.get_acc_number()} "
                  f"({converted_amount:.2f} {receiver_currency.name}) via Bank transfer")

            transaction.set_status(TransactionStatus.SUCCESS)

        except Exception as e:
            transaction.set_status(TransactionStatus.FAILED)
            print(f"Transaction failed: {e}")
            return transaction
        return transaction
