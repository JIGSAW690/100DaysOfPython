from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have out of {options}?\n").lower()
    if(choice=='off'):
        is_on = False
    elif(choice=='report'):
        # Print Report
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # Check resources are sufficient
        if coffee_maker.is_resource_sufficient(drink):
            # Process Coins
            # Check Transaction Successful
            if money_machine.make_payment(drink.cost):
                # Make Coffee
                coffee_maker.make_coffee(drink)






