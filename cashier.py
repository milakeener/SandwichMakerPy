def process_coins():
    """Returns the total calculated from coins inserted.
       Hint: include input() function here, e.g. input("how many quarters?: ")"""
    large_dollars = int(input("How many large dollars would you like to insert?")) * 1.0;
    half_dollars = int(input("How many half dollars would you like to insert?: ")) * 0.50;
    quarters = int(input("How many quarters would you like to insert?: ")) * 0.25;
    nickels = int(input("How many nickels would you like to insert?: ")) *0.05;

    coins = (large_dollars * 1.0 +
             half_dollars * 0.50 +
             quarters * 0.25 +
             nickels * 0.05)

    return round(coins, 2)


def transaction_result(coins, cost):
    """Return True when the payment is accepted, or False if money is insufficient.
       Hint: use the output of process_coins() function for cost input"""
    if coins >= cost:
        change = round(coins - cost, 2)
        if change > 0:
            print(f"Order accepted! Here is ${change} in change.")
        else:
            print("Order accepted!")
        return True
    else:
        print("Sorry, that's not enough money. Payment refunded.")
        return False


class Cashier:
    def __init__(self):
        pass
