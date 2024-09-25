import data
import sandwich_maker
import cashier
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()




def main():
    machine = SandwichMaker(resources)
    while True:
        user_input = input("What would you like? (Small Sandwich/Medium Sandwich/Large Sandwich/Off/Report)")

        if user_input == "off":
            print("Turning off the machine.")
            break
        elif user_input == "report":
            machine.show_report()
        elif user_input in recipes:
            sandwich_ingredients = recipes[user_input]["ingredients"]
            sandwich_cost = recipes[user_input]["cost"]

            # Check if resources are sufficient
            if machine.check_resources(sandwich_ingredients):
                print("Please insert coins.")
                total_inserted = cashier.process_coins()

                # Check if the transaction is successful
                if cashier.transaction_result(total_inserted, sandwich_cost):
                    # Make the sandwich
                    machine.make_sandwich(user_input, sandwich_ingredients)


if __name__=="__main__":
    main()
