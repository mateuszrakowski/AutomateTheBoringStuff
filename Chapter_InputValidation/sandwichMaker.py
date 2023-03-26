import pyinputplus as pyip


menu = {
    "bread": {"wheat": 1, "white": 1.50, "sourdough": 2},
    "protein": {"chicken": 5, "turkey": 6, "ham": 3, "tofu": 5},
    "cheese": {"cheddar": 5, "Swiss": 6, "mozzarella": 8},
    "additives": {"mayo": 2, "mustard": 2.5, "lettuce": 3, "tomato": 4},
}


def sandwichesOrder():
    # Empty list to store ingredients of sandwiches
    sandwiches = []

    # Ask user for their preferred ingredients and store them inside list
    bread = pyip.inputMenu([key for key in menu["bread"]])
    sandwiches.append(bread)

    protein = pyip.inputMenu([key for key in menu["protein"]])
    sandwiches.append(protein)

    if pyip.inputYesNo("With cheese?\n") == "yes":
        cheese = pyip.inputMenu([key for key in menu["cheese"]])
        sandwiches.append(cheese)
    
    for additive in menu["additives"]:
        question = pyip.inputYesNo(f"Would you like a {additive}?\n")

        if question == "yes":
            sandwiches.append(additive)

    # Last element will be number of sandwiches
    sandwiches.append(pyip.inputInt(prompt="How many sandwiches?\n", min=1))

    return sandwiches

    
def sandwichesPrice(order):
    # Variable to count total price
    total = 0

    for ingredient in order:
        for k, v in menu.items():

            # Check if ingredient is inside each of [list] which contains each of the nested dictionary key, eg. ["wheat", "white", "sourdough"]
            # Used list comprehension here is crucial - it allows to use "if in" conditional statement as it creates a [list]
            if ingredient in [nestedKey for nestedKey in v]:
                
                # Variable 'k' represents menu primary key, eg. "bread"
                total += menu[k][ingredient]

    return f"Total price: {total * order[-1]}"


print(sandwichesPrice(sandwichesOrder()))