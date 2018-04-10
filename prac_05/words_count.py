"""
Program to count how many occurrence of a word in a phrase
"""

text = input("Please enter phrase : > ")
words = []
word_count = {}
i = 0
j = 0
words = text.split()
w_ct = len(words)
for i in range(0, w_ct-1, 1):
    word_count[words[i]] = 0

x = 0
for element in words:
    if words[x] in word_count:
        word_count[words[x]] += 1
    x = x + 1

for key, value in word_count.items():
    print("{:12} : {:3}".format(key, value))
