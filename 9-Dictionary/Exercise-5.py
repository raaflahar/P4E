'''
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.
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
        index = username.find('@')
        email_address = username[index+1:]
        if email_address not in new_dict:
            new_dict[email_address] = 1
        else:
            new_dict[email_address] += 1
print(new_dict)
