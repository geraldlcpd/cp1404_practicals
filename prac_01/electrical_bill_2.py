"""
Electricity Bill Estimator
"""

print("Electricity Bill Estimator")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

fare_choice = float(input("Which tariff (11 or 31)"))
while fare_choice != 11 or 31:
    print("Invalid input, Please Try again")
    fare_choice = float(input("Which tariff (11 or 31)"))

if fare_choice == 11:
    kwh_price = TARIFF_11
elif fare_choice == 31:
    kwh_price = TARIFF_31

daily_use = float(input("Enter daily use in kWH: "))
bill_days = float(input("Enter number of billing days: "))

total_bill = (daily_use * bill_days) * (kwh_price/100)
print("Estimated bill : $ {:.2f}".format(total_bill))

