'''
Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
'''

filename = input('Enter a file name: ')

try:
    file = open(filename)
except:
    print('This is not file in txt format, please try again!')
    exit()

dictionary = dict()

for line in file:
    line = line.rstrip()
    alphabet_character ='abcdefghijklmnopqrstuvwxyz'
    for word in line.lower():
        if word in alphabet_character:
            dictionary[word] = dictionary.get(word,0)+1

data = list()

for key,val in list(dictionary.items()):
    data.append((val,key))

data.sort(reverse=True)

for count,char in data:
    print(f'Count: {count} Letter: {char}')