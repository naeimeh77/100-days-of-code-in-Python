from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    # TODO 1. Prompt the user for input
    choice = input(f" What would you like? {menu.get_items()}: ")
    # Check the user's input
    if choice == "off":
        # TODO 2.Turn off the machine
        print("Turning off the machine...")
        break
    elif choice == "report":
        # TODO 3. Print the report
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(choice):
        # TODO 4. Check if there are enough resources to make the drink
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order):
            # Prompt the user to insert coins
            # TODO 5. Calculate the monetary value of the coins inserted
            cost = order.cost
            # TODO 6: check transaction successful
            if money_machine.make_payment(cost):
                # TODO 7. update the resources
                coffee_maker.make_coffee(order)






