from services.decorators import logger
from models.restaurant_model import Restaurant
from models.food_item_model import FoodItem


class RestaurantService:
    def __init__(self, repo):
        self.repo = repo

    @logger
    def add_restaurant(self):
        name = input("Enter restaurant name: ")
        location = input("Enter location: ")

        restaurant = Restaurant(name, location)

        while True:
            item_name = input("Food item name: ")
            price = float(input("Enter food price: "))

            food_item = FoodItem(item_name, price)

            restaurant.add_food_item(food_item)

            choice = input("Add another item? (y/n): ")

            if choice.lower() != "y":
                break

        self.repo.save_restaurant(restaurant)
        print("✅ Restaurant added")

    @logger
    def show_restaurants(self):
        restaurant = self.repo.find_all()

        if not restaurant:
            print("❌ No restaurant available")
            return

        for index, restaurant in enumerate(restaurant, start=1):
            print(f"\n{index}. {restaurant.name} - {restaurant.location}")

            for food in restaurant.food_items:
                print(f"   🍔 {food.name} - ₹{food.price}")
