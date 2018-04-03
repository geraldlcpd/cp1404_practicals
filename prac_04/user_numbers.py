"""
Program to ask user for 5 numbers and displays statistical information
"""

numbers = []
NUM_COUNT = 5
totals = 0
for NUM_COUNT in range(1, NUM_COUNT+1):
    num_input = float(input("Number: >> "))
    numbers.append(num_input)
    totals = totals + num_input

print("The First number is {:7}".format(numbers[0]))
print("The last number is {:8}".format(numbers[4]))


print("The Maximum value is {:6}".format(max(numbers)))
print("The minimum value is {:6}".format(min(numbers)))

print("Total value is {:13}".format(totals))
print("Average value is {:11.2f}".format(totals/5))