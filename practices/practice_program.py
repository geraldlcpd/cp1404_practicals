"""
ages_dict =  {'Bill':21, 'Jane':34, 'Jack':56}
name_input = input("Enter Name : >> ")
age_input = input("Enter Age: >> ")

ages_dict.update({name_input:age_input})
num_keys = len(ages_dict)

for key, value in ages_dict.items():
    print("{:8} - {:>6}".format(key, value))


"""

class Thing:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def change(self, b):
        self.a += b

it = Thing(5, 6)
it.change(2)
print(it.a, it.b)