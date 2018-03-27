user_name = input("Please Enter Your Name: >>> ")
while user_name == "":

    print("Error. Please Try Again")
    user_name = input("Please Enter Name: >>> ")

print(user_name[1])