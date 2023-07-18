'''
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dic-
tionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.
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

max_value = None
max_key = None

for key,value in new_dict.items():
    if max_value is None or value > max_value:
        max_value = value
        max_key = key
            
print(f'{max_key} {max_value}')
