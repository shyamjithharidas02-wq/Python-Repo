from payments.payment import Payment


class CardPayment(Payment):
    def pay(self, amount):
        print(f"💳 Paid {amount} using Card")
