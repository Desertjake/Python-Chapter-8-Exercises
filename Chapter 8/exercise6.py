#Garrett Chapter 8 

values = []
Still_Going = True

while Still_Going:
  newIn = input("Enter a number: \n")
  if newIn == "done":
    break
  else: 
    newIn = int(newIn)
    values.append(newIn)
    
print("The maximum value is: " + str(max(values)))

print("The minimum value is: " + str(min(values)))