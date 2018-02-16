#Garrett Chapter 8 Exercise 5

file = input("Enter a file name (suggested mbox-short.txt): ")

fhand = open(file)

count = 0 

for line in fhand:
  words = line.split()
  if len(words) == 0 : continue
  if words[0] != 'From' : continue
  print(words[1])
  if words[0] == 'From' : 
    count = count + 1

print ("There were " + str(count) + " lines in the file with From as the first word.")