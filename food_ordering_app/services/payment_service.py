from payments.upi_payment import UpiPayment
from payments.card_payment import CardPayment
from models.transaction_model import Transaction


class PaymentService:
    def process_payment(self, amount):
        print("\n1. UPI")
        print("2. Card")

        choice = input("Choose payment method: ")

        if choice == "1":
            payment = UpiPayment()
            payment_type = "UPI"
        else:
            payment = CardPayment()
            payment_type = "Card"

        payment.pay(amount)

        transaction = Transaction(amount, payment_type)

        print("\n✅ Transaction Successful")
        print(f"Transaction ID : {transaction.transaction_id}")
        print(f"Payment Type   : {transaction.payment_type}")
        print(f"Amount         : ₹{transaction.amount}")

        return transaction
