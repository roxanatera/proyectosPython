hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Checkpoint 1 Create a variable total_price, and set it to 0.
total_price = 0

#Checkpoint 2 Loop through the prices list and add each price to the variable total_price.
for total_price in prices:
  print(total_price)

#Checkpoint 3, create a variable called average_price that is the total_price divided by the number of prices.
average_price = total_price / len(prices)

#Checkpoint 4, Print the value of average_price.
print(average_price)

#Checkpoint 5, Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.
new_prices = [price - 5 for price in prices]

#Checkpoint 6, print.
print(new_prices)

#Checkpoint 7, Create a variable called total_revenue and set it to 0.
total_revenue = 0

#Checkpoint 8, Use a for loop to create a variable i.
for i in range(len(hairstyles)):
    print(i, hairstyles[i])

#Checkpoint 9, Add the product of prices[i].
for i in range(len(prices)):
    total_revenue += prices[i] * last_week[i]

#Checkpoint 10, After your loop, print the value of total_revenue. Total Revenue: <total_revenue>
print(f'Total revenue: {total_revenue}')

#Checkpoint 11, Find the average daily revenue by dividing total_revenue by 7.
average_daily_revenue = total_revenue / 7
print(f'Average daily revenue: {average_daily_revenue}')

#Checkpoint 12, 
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

#Checkpoint 13, print.
print(cuts_under_30)



