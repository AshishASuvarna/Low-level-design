from threading import RLock


class Account:
    def __init__(self,acc_number,user_id,balance,currency):
        self.acc_number=acc_number
        self.user_id=user_id
        self.balance=balance
        self.currency=currency
        self._lock=RLock()

    def deposit(self,amount):
        if amount<=0:
            raise Exception("Amount should be positive")
        with self._lock:
            self.balance+=amount
            return self.balance


    def withdraw(self,amount):
        if amount>=self.balance:
            raise Exception("Low Balance")

        with self._lock:
            self.balance-=amount
            if self.balance - amount < 50:
                raise Exception(f"Balance below $50. Current bal:{self.balance}")
            self.balance -= amount
            return self.balance

    def get_acc_number(self):
        return self.acc_number

    def get_balance(self):
        return self.balance

    def get_currency(self):
        return self.currency

    def get_user_id(self):
        return self.user_id