class Order:
    def __init__(self, user, item, quantity, total):
        self.user = user
        self.item = item
        self.quantity = quantity
        self.total = total
        self.status = "PENDING"
