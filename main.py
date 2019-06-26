uitleg = "..."
print(uitleg)

#random getalen reeks pakken
from random import randint
code = []
for i in range(0, 4):
  code.append((randint(0,6)))
print(code)

#niput van user vragen
userInput = input("geef")
print(userInput)
#check input
if userInput == randomcode:
  print ("Good job! You cracked the code!")
else :
  print ("Try again!")
