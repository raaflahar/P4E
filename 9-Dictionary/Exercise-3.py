'''
Exercise 3: Write a program to read through a mail log, build a his-
togram using a dictionary to count how many messages have come from
each email address, and print the dictionary.
'''

filename = input('Enter file name: ')

try:
     new_file = open(filename)
except:
    print('This is not a file, please try again!')

new_dict = dict()

for line in new_file:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        username = words[1]
        if username not in new_dict:
            new_dict[username] = 1
        else:
            new_dict[username] += 1
print(new_dict)