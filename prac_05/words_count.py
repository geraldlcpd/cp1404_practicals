"""
Program to count how many occurrence of a word in a phrase
"""

text = input("Please enter phrase : > ")
words = []
word_count = {}
i = 0

words = text.split()
words.sort()

w_ct = len(words)
for i in range(0, w_ct-1, 1):
    word_count[words[i]] = 0

i = 0
for element in words:
    if words[i] in word_count:
        word_count[words[i]] += 1
    i = i + 1
for key, value in word_count.items():
    print("{:12} : {:3}".format(key, value))
