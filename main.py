uitleg = "..."
print(uitleg)

#random getalen code maken
from random import randint
code = []
for i in range(0, 4):
  code.append((randint(0,6)))
print(code)

#niput van user vragen
UserInput = input("Type your guess: ")
print(UserInput)
if UserInput == code:
  print ("You solved the code!")
else:
  print ("hoi")
