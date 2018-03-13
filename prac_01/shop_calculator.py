"""
Program for entering discount information after user inputs how many items and how much are each

"""

num_items = int(input("Number of Items: "))
while num_items < 0:
    print("Invalid Input. Please Try again")
    num_items = int(input("Number of Items: "))
total_price = 0
for i in range (0,num_items,1):
    item_price = float(input("Price of item: $ "))
    total_price = total_price + item_price

if total_price > 100:
    total_price = 0.9 * total_price


print("Total Price for", num_items, "items is: $ {:.2f} ".format(total_price))