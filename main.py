# This is a program that mimics the Domino's online pizza creation tool.
# It asks for user input on pizza components and returns a price at the end.

import pyinputplus as pyip


def store_locator():  # This can be improved to actually return a list of Domino's stores close to the given address.
    pizza_transport = pyip.inputMenu(['Delivery', 'Carryout'], "How do you want your Domino's today?\n", numbered=True)
    print(pizza_transport)
    if pizza_transport == 'Delivery':
        address_type = pyip.inputMenu(['House', 'Apartment', 'Business', 'Campus', 'Base', 'Hotel', 'Other'],
                                      "Address Type\n", numbered=True)
        print(address_type)
        if address_type in ['Apartment', 'Campus', 'Hotel']:
            suite_apt_num = pyip.inputNum(prompt="What is your suite or apartment number?:\t")
        street_address = pyip.inputStr(prompt="Please type your street address:\t")
        zip_code = pyip.inputNum(prompt="What is your zip code?: \t")
        city = pyip.inputStr(prompt="What city do you live in?: \t")
        state = pyip.inputStr(prompt="What state do you live in?: \t")
    else:
        zip_code = pyip.inputNum(prompt="What is your zip code?: \t")
        city = pyip.inputStr(prompt="What city do you live in?: \t")
        state = pyip.inputStr(prompt="What state do you live in?: \t")

    ## In the future search the web for a list of dominoes stores close to the address.


def pizza_builder():
    pizza_size = pyip.inputMenu(['Small - 10"', 'Medium - 12"', 'Large - 14"', 'X-Large - 16"'],
                                prompt='Choose your pizza size: \n', numbered=True)
    crust_type = pyip.inputMenu(['Brooklyn Style - Hand stretched to be big, thin and perfectly foldable.',
                                 'Hand Tossed - Garlic-seasoned crust with a rich buttery taste.',
                                 'Crunchy Thin Crust - Thin enough for the optimum crispy to crunchy ratio and '
                                 'square cut to be perfectly shareable'], numbered=True)
    quantity = pyip.inputNum(prompt="How many of these pizzas do you want to enjoy?\t")
    cheese_size = pyip.inputMenu(['None', 'Light', 'Normal', 'Extra', 'Double'],
                                 prompt="How much cheese do you want?\n", numbered=True)
    sauce_type = pyip.inputMenu(['Robust Inspired Tomato Sauce', 'Hearty Marina Sauce', 'Honey BBQ Sauce',
                                 'Garlic Parmesan Sauce', 'Alfredo Sauce', 'Ranch'],
                                prompt="What kind of sauce do you want?\n", numbered=True)
    sauce_quantity = pyip.inputMenu(['Light', 'Normal', 'Extra'], prompt="How much of that sauce do you want?\n",
                                    numbered=True)

    customer_meat_selection = {}
    another_topping = 'yes'
    while another_topping == 'yes':
        meat_type = pyip.inputMenu(['Ham', 'Beef', 'Salami', 'Pepperoni', 'Italian Sausage', 'Premium Chicken',
                                    'Bacon', 'Philly Steak', 'No meat please.'],
                                   prompt='Please select a topping.\n', numbered=True)
        if meat_type == 'No meat please.':
            break
        meat_quantity = pyip.inputMenu(['Light', 'Normal', 'Extra', 'Double'],
                                       prompt="How much of that meat do you want\n", numbered=True)
        customer_meat_selection[meat_type] = meat_quantity
        another_topping = pyip.inputYesNo(prompt="Would you like to add another meat, yes or no?")

    customer_non_meat_selection = {}
    another_topping = 'yes'
    while another_topping == 'yes':
        topping_type = pyip.inputMenu(['Hot Buffalo Sauce', 'Jalapeno Peppers', 'Onions', 'Banana Peppers',
                                       'Diced Tomatoes', 'Black Olives', 'Mushrooms', 'Pineapple',
                                       'Shredded Provolone Cheese', 'Cheddar Cheese', 'Green Peppers',
                                       'Spinach', 'Roasted Red Peppers', 'Feta Cheese', 'Shredded Parmesan Asiago',
                                       'No toppings for me thanks.'],
                                      prompt='Please select a topping.\n', numbered=True)
        if topping_type == 'No toppings for me thanks.':
            break
        topping_quantity = pyip.inputMenu(['Light', 'Normal', 'Extra', 'Double'],
                                          prompt="How much of that topping do you want\n", numbered=True)
        customer_non_meat_selection[topping_type] = topping_quantity
        another_topping = pyip.inputYesNo(prompt="Would you like to add another topping, yes or no?")


    customer_sides = []
    another_side = 'yes':
    while another_side == 'yes':
        side_type = pyip.inputMenu(['Ranch', 'Garlic Dipping Sauce', 'Marinara Dipping Sauce', 'No side for me today.'],
                                   prompt="What kind of side would you like?", numbered=True)
        customer_sides.append(side_type)
        if side_type == 'No side for me today.':
            break

    return pizza_size, crust_type, quantity, cheese_size, sauce_type, sauce_quantity, customer_meat_selection, \
           customer_non_meat_selection, customer_sides

def  calculate_pizza_order():







# run functions
print(pizza_builder())
