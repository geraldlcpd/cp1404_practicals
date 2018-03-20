name = "Gibson"
year = 1922
cost = 16035.40
print("---Program 1 Trial---")
print("My guitar: {}, first made in {}".format(name,year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name,year))
print("My {} would cost ${:,.2f}".format(name, cost))


print(" ")
print("---Program 2 Trial---")

numbers = [1,19,123,456, -25]
for i in range(len(numbers)):
    print("Number {0} is {1:>5}".format(i+1, numbers[i]))

print(" ")
print("---Program 3 Trial---")

num2 = [0,50,100]
for i in range(len(num2)):
    print("{1:>4}".format(i+1, num2[i]))


print(" ")
print("---Example to Study---")

import random
MAX_INCREASE = 0.1  #10% increase
MAX_DECREASE = 0.05 # 5% decrease
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
print("$ {:,.2f}".format(price))


while price >= MIN_PRICE and price <= MAX_PRICE:
    NUM_DAYS = 425
    for i in range (0, NUM_DAYS, 1):
        price_change = 0
    # Random Num Gen of 1 or 2
    # if Rand_Gen = 1, price increases, if it is 2, price decrease
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        print("On day {0} Price is $ {1:,.2f}".format(i+1, price))