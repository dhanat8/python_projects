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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def ask_user():
    """Ask for user's input"""
    global restart, machine_stop, can_check_resource
    restart = True
    can_check_resource = False
    machine_stop = False
    user_choice = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    if user_choice =="espresso" or user_choice =="latte" or user_choice =="cappuccino":
        can_check_resource = True
        return user_choice
    elif user_choice == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")
        print(f"Revenue: {money}")
        restart_machine()
    elif user_choice == "off":
        print("Bye")
        restart = False
    else:
        print("You put in a wrong menu")
        restart_machine()

def check_resources(user_choice):
    """Check if resources are available"""
    global can_check_money
    can_check_money = False
    ingredients_required = {}
    unavailable_items = []
    for each_ingredient in MENU[user_choice]['ingredients']:
        ingredients_required[each_ingredient] = MENU[user_choice]['ingredients'][each_ingredient]

    for each_item in ingredients_required:
        if resources[each_item] >= ingredients_required[each_item]:
            can_check_money = True
            return
        elif resources[each_item] < ingredients_required[each_item]:
            unavailable_items.append(each_item)
            if len(unavailable_items) == 1:
                print(f"Sorry we don't have enough {unavailable_items[0]}")
                restart_machine()
                return
            elif len(unavailable_items) == 2:
                print(f"Sorry we don't have enough {unavailable_items[0]} and {unavailable_items[1]}.")
                restart_machine()
                return
            elif len(unavailable_items) == 3:
                print(f"Sorry we don't have enough {unavailable_items[0]}, {unavailable_items[1]}, and {unavailable_items[2]} ")
                restart_machine()
                return
            # don't forget to check if they want to order again

def make_coffee(user_choice):
    global resources
    ingredients_required = {}
    for each_ingredient in MENU[user_choice]['ingredients']:
        ingredients_required[each_ingredient] = MENU[user_choice]['ingredients'][each_ingredient]
    for item in ingredients_required:
        resources[item] -= ingredients_required[item]
    print(f"Here is your {user_choice} ☕️. Enjoy!")
    restart_machine()

def check_money(user_choice):
    global can_make_coffee, machine_stop
    can_make_coffee = False
    machine_stop = False
    restart_money = True
    while restart_money:
        quarter = int(input("How many quarters?"))
        dime = int(input("How many dimes?"))
        nickel = int(input("How many nickels?"))
        penny = int(input("How many pennies?"))
        total_money = quarter*0.25 + dime*0.10 + nickel*0.05 + penny*0.01
        print(f"Your total money is {round(total_money,2)}")
        coffee_cost = MENU[user_choice]['cost']
        if total_money > coffee_cost:
            print(f"Here is your change of ${round(total_money-MENU[user_choice]['cost'],2)}.")
            restart_money = False
            can_make_coffee = True
            return coffee_cost
        elif total_money == coffee_cost:
            restart_money = False
            can_make_coffee = True
            return coffee_cost
        else:
            print("Sorry, there is not enough_money. Money returned.")
            restart = input("Do you want to insert money again? Y or N\n").lower()
            if restart == "n":
                restart_money = False
                machine_stop = True
            elif restart == "y":
                restart_money = True
                pass
                # Don't forget to close the machine

def restart_machine():
    global restart
    restart = True
    restart_or_not = input("Do you want to start again? Y or N\n").lower()
    if restart_or_not == "y":
        restart = True
    elif restart_or_not == "n":
        print("Thank you and good bye!")
        restart = False

restart = True
can_check_resource = False
can_check_money = False
can_make_coffee = False
machine_stop = False

while restart and not machine_stop:
    user_choice = ask_user()
    if can_check_resource:
        check_resources(user_choice=user_choice)
        if can_check_money:
            rev = check_money(user_choice=user_choice)
            if machine_stop == False:
                money += rev
            if can_make_coffee:
                make_coffee(user_choice=user_choice)















