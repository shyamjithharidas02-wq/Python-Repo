from repositories.user_repository import UserRepository
from repositories.restaurant_repository import RestaurantRepository
from repositories.order_repository import OrderRepository

from services.auth_service import AuthService
from services.restaurant_service import RestaurantService
from services.order_service import OrderService

from models.food_item_model import FoodItem

from models.user_model import User

user_repo = UserRepository()
restaurant_repo = RestaurantRepository()
order_repo = OrderRepository()


auth_service = AuthService(user_repo)
restaurant_service = RestaurantService(restaurant_repo)
order_service = OrderService(auth_service, restaurant_repo, order_repo)


# SAMPLE DATA
restaurant_service.repo.save_restaurant(
    __import__("models.restaurant_model").restaurant_model.Restaurant("KFC", "Kochi")
)

restaurant = restaurant_repo.find_all()[0]


restaurant.add_food_item(FoodItem("Burger", 120))
restaurant.add_food_item(FoodItem("Chicken Fry", 220))
restaurant.add_food_item(FoodItem("Pepsi", 40))


while True:

    print("\n========== FOOD ORDERING APP ==========")
    print("1. Register")
    print("2. Login")
    print("3. View Restaurants")
    print("4. Place Order")
    print("5. View Orders")
    print("6. Total Users")
    print("7. Logout")
    print("8. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        auth_service.register()

    elif choice == "2":
        auth_service.login()

    elif choice == "3":
        restaurant_service.show_restaurants()

    elif choice == "4":
        order_service.place_order()

    elif choice == "5":
        order_service.show_orders()

    elif choice == "6":
        User.get_total_users()

    elif choice == "7":
        auth_service.logout()

    elif choice == "8":
        print("👋 Exiting Application")
        break

    else:
        print("❌ Invalid Choice")
