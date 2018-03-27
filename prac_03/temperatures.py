"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def c_to_f(c_input):
    """Determine Fahrenheit from Celsius input"""
    fahrenheit = c_input * (9.0 / 5) + 32
    return fahrenheit


def f_to_c(f_input):
    """Determine Celsius from Fehrenheit input"""
    celsius = (f_input - 32) * (5 / 9)
    return celsius


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius"""

print(MENU)
choice = input(">>> ").upper()
if choice == "C":
    temp_input = float(input("Enter Celsius : >> "))
    result = c_to_f(temp_input)
    print("Fahrenheit: {:.2f} ".format(result))
elif choice == "F":
    temp_input = float(input("Enter Fahrenheit: >> "))
    result = f_to_c(temp_input)
    print("Celsius: {:.2f}".format(result))

