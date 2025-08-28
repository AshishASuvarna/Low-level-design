class Transaction:
    def __init__(self,transaction_id,timestamp,amount,currency,sender,receiver,status):
        self.transaction_id=transaction_id
        self.timestamp=timestamp
        self.amount=amount
        self.currency=currency
        self.sender=sender
        self.receiver=receiver
        self.status=status

    def get_transaction_id(self):
        return self.transaction_id

    def get_timestamp(self):
        return self.timestamp

    def get_currency(self):
        return self.currency

    def get_amount(self):
        return self.amount

    def get_sender(self):
        return self.sender

    def get_receiver(self):
        return self.receiver

    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status

