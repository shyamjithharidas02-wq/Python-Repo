from models.order_model import Order
from services.decorators import logger, login_required, timer
from services.payment_service import PaymentService


class OrderService:

    def __init__(self, auth_service, restaurant_repo, order_repo):

        self.auth_service = auth_service
        self.restaurant_repo = restaurant_repo
        self.order_repo = order_repo

    @property
    def current_user(self):
        return self.auth_service.current_user

    @logger
    @login_required
    @timer
    def place_order(self):

        restaurants = self.restaurant_repo.find_all()

        if not restaurants:
            print("❌ No restaurants available")
            return

        print("\n===== RESTAURANTS =====")

        for index, restaurant in enumerate(restaurants, start=1):
            print(f"{index}. {restaurant.name}")

        restaurant_choice = int(input("Choose restaurant: ")) - 1

        restaurant = restaurants[restaurant_choice]

        print(f"\n===== {restaurant.name} MENU =====")

        for index, food in enumerate(restaurant.food_items, start=1):
            print(f"{index}. {food.name} - ₹{food.price}")

        food_choice = int(input("Choose food item: ")) - 1

        food_item = restaurant.food_items[food_choice]

        quantity = int(input("Quantity: "))

        total = food_item.price * quantity

        print(f"\n💰 Total Amount: ₹{total}")

        payment_service = PaymentService()

        payment_service.process_payment(total)

        order = Order(self.current_user, food_item.name, quantity, total)

        self.order_repo.save_orders(order)

        print("\n✅ Order Placed Successfully")
        print(f"Item     : {order.item}")
        print(f"Quantity : {order.quantity}")
        print(f"Total    : ₹{order.total}")
        print(f"Status   : {order.status}")

    @logger
    @login_required
    def show_orders(self):

        orders = self.order_repo.find_all()

        if not orders:
            print("❌ No orders available")
            return

        print("\n===== ALL ORDERS =====")

        for order in orders:
            print(
                f"👤 {order.user.name} | "
                f"🍔 {order.item} | "
                f"Qty: {order.quantity} | "
                f"₹{order.total} | "
                f"{order.status}"
            )
