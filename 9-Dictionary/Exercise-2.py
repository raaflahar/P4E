'''
Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
'''

file = input('Enter a file name: ')

try:
    filename = open(file)
except:
    print('This was not a file, please try again!')
    exit()

new_dict = dict()

for line in filename:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        day = words[2]
        if day not in new_dict:
            new_dict[day] = 1
        else:
            new_dict[day] += 1

print(new_dict)
