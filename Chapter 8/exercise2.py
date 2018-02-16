#Garrett Chapter 8 Exercise 2

fhand = open('mbox-short.txt')

count = 0

for line in fhand:
    words = line.split()
    
    if len(words) == 0 : continue
    if words[0] != 'From': 
      continue
    if len(words) > 2:
      print(words[2])