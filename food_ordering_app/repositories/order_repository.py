class OrderRepository:
    def __init__(self):
        self.orders = []

    def save_orders(self, order):
        self.orders.append(order)

    def find_all(self):
        return self.orders
