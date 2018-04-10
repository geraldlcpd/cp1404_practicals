import random
pick_amount = int(input("How many quick picks? >> "))


i = 0
for pick_amount in range(1, pick_amount+1, 1):
    numbers = []
    for i in range(1, 6, 1):
        number_generate = random.randint(1, 45)
        if number_generate in numbers:
            numbers.remove(number_generate)
            number_generate = random.randint(1, 45)
            i = i-1
        else:
            numbers.append(number_generate)
    print(numbers)



