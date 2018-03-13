score = float(input("Enter Score: "))
if score < 0:
    print("Invalid Score")
elif score > 100:
    print("Invalid Score")
elif score > 90:
    print("Excellent")
elif score > 50:
    print("Passable")
else:
    print("Bad")
