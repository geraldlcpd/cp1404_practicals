"""
Program to look up hex color value based on user input
"""

COLOR_DICT = {'Black': "#000000", 'White': '#FFFFFF', 'Cyan': '#00FFFF', 'Red': '#FF0000', 'Green': '#00FF00', 'Yellow': '#FF0000', 'Blue': '#0000FF', 'Orange': '#FFA500', 'AliceBlue': '#F0F8FF'}

color_choice = input("Input Color Name : >> ")
while color_choice not in COLOR_DICT:
    print("Color not yet in dictionary. Please try another one")
    color_choice = input("Input Color Name: >> ")
print(color_choice, " is [", COLOR_DICT[color_choice], "]")

