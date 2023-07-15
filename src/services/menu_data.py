import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.reader(source_path)

    def reader(self, file_path):
        with open(file_path, newline='') as file:
            open_file = csv.reader(file)
            next(open_file)

            for row in open_file:
                dish_name, price, ingredient, amount = row[:4]
                create_dish = Dish(dish_name, float(price))
                new_ingredient = Ingredient(ingredient)
                new_dish = self.find_dish(create_dish)
                new_dish.add_ingredient_dependency(new_ingredient, int(amount))

    def find_dish(self, dish: Dish):
        for exist_dish in self.dishes:
            if exist_dish == dish:
                return exist_dish

        self.dishes.add(dish)
        return dish
