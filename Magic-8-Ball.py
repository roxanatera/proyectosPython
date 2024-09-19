import random
name = "Julia"
question = "Si"
answer = ""
random_number = random.randint(1, 9)

if random_number == 1:
  answer = "Yes definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "It is decidedly so"
elif random_number == 6:
  answer = "It is decidedly so"
elif random_number == 7:
  answer = "It is decidedly so"
elif random_number == 8:
  answer = "It is decidedly so"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

print(f"{name} asks: {question}")
print(f"Magic 8-Ball's: answer: {answer}")
