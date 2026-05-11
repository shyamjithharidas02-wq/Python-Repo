import random


class Transaction:
    def __init__(self, amount, payment_type):
        self.amount = amount
        self.payment_type = payment_type
        self.status = "SUCCESS"
        self.transaction_id = random.randint(10000, 99999)
