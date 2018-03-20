try:
    numerator = int(input("Enter Numerator:  "))
    denominator = int(input("Enter Denominator:  "))

    while denominator == 0:
        print("Cannot divide by Zero! Please Try again")
        denominator = int(input("Enter Denominator:  "))

    fraction = numerator / denominator
    print(fraction)


except ValueError:
    print("Numerator and Denominator must be valid numbers")


print("Finished")