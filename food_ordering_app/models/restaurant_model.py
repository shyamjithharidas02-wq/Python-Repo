class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.food_items = []

    def add_food_item(self, food_item):
        self.food_items.append(food_item)
