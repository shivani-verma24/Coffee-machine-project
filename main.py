MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

while (True):

    flavor = input("What would you like? (espresso/latte/cappuccino): ")
    if (flavor == 'off'):
        break

    elif (flavor == 'report'):
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    else:

        order_ingredients = MENU[flavor]["ingredients"]
        if is_resource_sufficient(order_ingredients):

            print("Please insert coins.")
            total = int(input("how many quarters?: ")) * 0.25
            total += int(input("how many dimes?: ")) * 0.1
            total += int(input("how many nickles?: ")) * 0.05
            total += int(input("how many pennies?: ")) * 0.01

            cost = MENU[flavor]['cost']
            if (total >= cost):
                left = round(total - cost, 2)
                print(f"Here is ${left} in change.")
                money += cost

                for item in order_ingredients:
                    resources[item] -= order_ingredients[item]
                print(f"Here is your {flavor} ☕️. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")


# Project by Shivani Verma