#Garrett Chapter 8 Exercise 4

wordslist = []

input = input("Enter file name (suggested romeo.txt): ")

fileo = open(input)

for line in fileo:
	for word in line.split():
		if word not in wordslist:
			wordslist.append(word)

wordslist.sort()

print (wordslist)