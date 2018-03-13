"""
Electricity Bill Estimator
"""

print("ELECTRICITY BILL ESTIMATOR PROGRAM")

kwh_price = float(input("Enter price per kWH in cents: "))
daily_use = float(input("Enter daily use in kWH: "))
bill_days = float(input("Enter number of billing days: "))

total_bill = (daily_use * bill_days) * (kwh_price/100)
print("Estimated bill : $ {:.2f}".format(total_bill))

