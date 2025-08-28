from threading import Lock

from User import User
from Account import Account
from PaymentMethod import *
from Conversion import Conversion
from Currency import Currency
from Transaction import Transaction


class Wallet:
    _instance=None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.initialized=False

        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def __init__(self):
        if not self.initialized:
            self.users={}
            self.accounts={}
            self.transaction=[]
            self._lock=Lock()
            self.initialized=True

    def register_users(self,user):
        with self._lock:
            self.users[user.get_id()]=user
            for acc in user.accounts.values():
                self.accounts[acc.get_acc_number()] = acc

    def remove_user(self,user):
        with self._lock:
            self.users.pop(user.get_id())


    def transfer_fund(self,sender_account_number,receiver_account_number,amount,payment_method):
        with self._lock:
            sender_acc=self.accounts.get(sender_account_number)
            receiver_acc=self.accounts.get(receiver_account_number)

            if not sender_acc or not receiver_acc:
                raise Exception("Invalid sender or receiver account number.")
            # Order locks by account number to avoid deadlocks
            a, b = sorted([sender_acc, receiver_acc], key=lambda acc: acc.get_acc_number())

            with a._lock:
                with b._lock:
                    transaction=payment_method.pay(amount,sender_acc,receiver_acc)
        with self._lock:
            self.transaction.append(transaction)

        print(f"Transaction {transaction.get_transaction_id()} recorded.")

        return transaction