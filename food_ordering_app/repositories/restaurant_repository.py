class RestaurantRepository:
    def __init__(self):
        self.restaurants = []

    def save_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def find_all(self):
        return self.restaurants
