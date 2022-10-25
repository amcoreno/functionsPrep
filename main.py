from add import add_fruit
from divide import divide_fruit
from multiply import multiply_fruit
apples = int(input("How many apples?"))
oranges = int(input("How many oranges?"))


# function call for adding apples and oranges

fruit = add_fruit(apples,oranges)


# function for dividing apples and oranges

divide = divide_fruit(apples,oranges)

# functions for multiplying apples and oranges

multiply = multiply_fruit(apples,oranges)

print(fruit)
print(divide)
print(multiply)