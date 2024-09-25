

class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount_needed in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < amount_needed:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        ########
        for ingredient, amount_needed in order_ingredients.items():
            self.machine_resources[ingredient] -= amount_needed
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")

    def show_report(self):
        print("Current resources: ")
        for ingredient, amount_needed in self.machine_resources.items():
            print(f"{ingredient}: {amount_needed}")
