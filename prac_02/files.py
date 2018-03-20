'''
print("---Program 1---")
OUTPUT_FILE = "name.txt"

file_out = open(OUTPUT_FILE, 'w')

name = input("Please Enter Name: ")
print("{0}".format(name), file = file_out)
print("Your name is {0}".format(name))

print("---Program 2---")
INPUT_FILE = "name.txt"
file_in = open(INPUT_FILE, 'r')
file_read = file_in.read()

print("Your name is {0}".format(file_read))

print("===Program 3===")
IN_FILE = "numbers.txt"
numfile_in = open(IN_FILE, 'r')

total_nums = 0
for line in numfile_in:
    num = int(line)
    total_nums = total_nums + num



print(total_nums)
'''
MIN_LENGTH = 5
MAX_LENGTH = 15

PASS_ACCEPTED = False

SPC_CHAR = "!@#$%^&*()_-=+`~,./'[]<>?{}|"
print("===Program 4===")
print("Please enter a valid password. Your password must be between 5 and 15 characters, and contain:")
print("     1 or more uppercase characters")
print("     1 or more lowercase characters")
print("     1 or more numbers, and")
print("     1 or more special characters")

pass_in = input("Please enter a Password: > ")
pass_count_chars = len(pass_in)

'''
pass_lower = pass_in.islower()
pass_upper = pass_in.isupper()
pass_numcount = pass_in.isnumeric()
'''

num_count = 0
low_count = 0
upp_count = 0
spc_count = 0
for char in pass_in:
    if char.isdigit():
        num_count = num_count + 1
    elif char.islower():
        low_count = low_count + 1
    elif char.isupper():
        upp_count = upp_count + 1
    elif char in SPC_CHAR:
        spc_count = spc_count + 1

while num_count == 0 or low_count == 0 or upp_count == 0 or spc_count == 0 or pass_count_chars < MIN_LENGTH or pass_count_chars > MAX_LENGTH:
    print("Password Invalid. Please Enter again")
    pass_in = input(("> "))

PASS_ACCEPTED = True
print("Your {0} character password is valid: {1}".format(pass_count_chars, pass_in))


