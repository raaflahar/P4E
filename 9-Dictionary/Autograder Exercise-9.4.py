'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

new_dict = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        username = words[1]
        if username not in new_dict:
            new_dict[username] = 1
        else:
            new_dict[username] += 1
            
max_value = 0
max_key = 0

for key,value in new_dict.items():
    if value > max_value:
        max_value = value
        max_key = key
        
print(f'{max_key} {max_value}')