'''
Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the num-
ber of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.
'''

filename = input('Enter your file: ')

try:
    file = open(filename)
except:
    print('This was not file, please try again!')
    exit()

dictio = dict()

for line in file:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        username = words[1]
        index = username.find('@')
        for email_address in username:
            email_address = username[index+1:]
            dictio[email_address] = dictio.get(email_address,0) + 1

data = list()
for key,val in list(dictio.items()):
    data.append((val,key)) #Parenthess for making two values into one value inside Tuples

data.sort(reverse=True)

print(data[0])