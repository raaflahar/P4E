'''
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn't matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.
'''

filename = open('words.txt')

new_dict = dict()

for line in filename:
    line = line.rstrip()
    new_dict[line] == 'Word'

print(new_dict)
