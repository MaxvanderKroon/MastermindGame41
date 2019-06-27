print("In this game you will try to crack a code! The computer will tell you how many numbers are in the right place or correct bu not in the right spot. You got 10 chances to crack the code! Good luck!")

from random import randint
code = []
for i in range(0, 4):
  code.append((randint(0,6)))
print(code)

while True:
  UserInput = input("Type your guess: ")
  if UserInput == code:
    print("You solved the code!")
  else:
    g = 0
    for j in range(0, 4):
      if str(code[j]) == (UserInput[j]):
        g = g + 1
    if g != 4:
      print(str(g) + " numbers are in the right place")
      f = 0
      for k in range(0, 4):
        if int(UserInput[k]) in code:
          f = f + 1
      f = f - g
      print(str(f) + " numbers are correct but not in the right spot")
