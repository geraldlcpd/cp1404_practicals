import random
MAX_INCREASE = 0.1  #10% increase
MAX_DECREASE = 0.05 # 5% decrease
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "py_try.txt"

price = INITIAL_PRICE
print("Starting Price: " + "$ {:,.2f}".format(price))
NUM_DAYS = 424
count_days = 1

out_file = open(OUTPUT_FILE, 'w')
for i in range (0, NUM_DAYS, 1):
    while price >= MIN_PRICE and price <= MAX_PRICE:

        price_change = 0
    # Random Num Gen of 1 or 2
    # if Rand_Gen = 1, price increases, if it is 2, price decrease
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0),


        count_days = count_days + 1
        price *= (1 + price_change)
        print("On day {0} Price is $ {1:,.2f}".format(count_days, price), file = out_file)

out_file.close()