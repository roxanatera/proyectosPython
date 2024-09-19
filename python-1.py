##Statement Break and continue

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
#print number +
for i in big_number_list:
  if i <= 0:
    continue
  print(i)

#Checkpoint 2.
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
    if age < 21:
        continue
    print(age)

numbers = [2, 4, 6, 8]
for number in numbers:
  print("hello!")

numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    break
  print(number)

for i in range(3):
  print(i)

drink_choices = ["coffee", "tea", "water", "juice", "soda"]
for drink in drink_choices:
  print(drink)

from datetime import datetime
birthday = datetime (1990, 12, 21)
birthday.year