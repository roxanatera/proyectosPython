# Your code below:
##Checkpoint 1
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

##checkpoint 2 prices list
prices = [2, 6, 1, 3, 2, 7, 2]

##Checkpoint 3 Count the number of occurrences 2
num_two_dollar_slices = prices.count(2)

#Checkpoin 4 the length of the toppings list
num_pizzas = len(toppings)
#print()

##Checkpoint 5, Print the string.
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

##checkpoint 6, create a new two-dimensional list called pizza_and_prices.
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

#checkpoint 7 print
print(pizza_and_prices)

##Checkpoint 8, Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).
pizza_and_prices.sort()
print(pizza_and_prices)

##Checkpoint 9, Store the first element of pizza_and_prices in a variable called cheapest_pizza.
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)

##Checkpoint 10, Get the last item of the pizza_and_prices list.
priciest_pizza = pizza_and_prices[-1]
#print(priciest_pizza)

##Checkpoint 11, To remove the last element of a list, use the .pop() method.
pizza_and_prices.pop()
#print(pizza_and_prices)

##Checkpoint 12, Add the new peppers pizza topping to our list.
pizza_and_prices.insert(4, [2.5, "peppers"])
#print(pizza_and_prices)

##Checkpoint 13,To get the first n items of a list, use list[:n].
three_cheapest = pizza_and_prices[:3]
#print checkpoint 14.
print(three_cheapest)






