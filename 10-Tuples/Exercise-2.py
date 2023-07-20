'''
Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. 
Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
'''

filename = input('Enter a file name: ')

try:
    file = open(filename)
except:
    print('This is not file format (txt), Please try again!')
    exit()

dictionary = dict()

for line in file:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()

print(words)