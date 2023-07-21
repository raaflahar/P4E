'''
Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
'''

filename = input('Enter file name: ')

try:
    file = open(filename)
except:
    print('This was not file, please try again!')
    exit()

dictionary = dict()

for line in file:
    line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        times = words[5]
        index = times.find(':')
        for time in times:
            time = times[index-2:index]
            dictionary[time] = dictionary.get(time,0)+1

data = list(dictionary.items())
data.sort()
for key,val in data:
    print(key,val)