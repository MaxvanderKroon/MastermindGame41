print("In this game you must try to crack the code! The computer will tell you how many numbers are in the spot, or correct but not in the right spot. You have 10 chances to crack the code. The code is 4 numbers long. Good luck!")

while True:
  
  from random import randint
  code = []
  for i in range(0, 4):
    code.append((randint(0,9)))
  i = 10
  i > 10
  while True:
    UserInput = input("Type your guess: ")
    if UserInput == '1955' :
      print("You guessed the birthyear of Mr. Bent!")
      i = i + 1
    if UserInput == '1980':
      print("You guessed the birthyear of Mr. Logtenberg!")
      i = i + 1
    if UserInput == code:
      print("You solved the code!")
    if len(UserInput) != 4:
      print("Error: Your Input must consist of 4 characters.")
      i = i - 1
      print(str(i) + " chances left")
      continue
    if not UserInput.isdigit():
      print('Error: Your Input should be only numbers.')
      i = i - 1
      print(str(i) + " chances left.")
      continue
    else:
      g = 0
      for j in range(0, 4):
        if str(code[j]) == (UserInput[j]):
          g = g + 1
      if g != 4:
        print(str(g) + " numbers are in the right place.")
        f = 0
        codelist = []
        for m in code:
          codelist.append(m)
        for k in range(0, 4):
          if int(UserInput[k]) in codelist:
            codelist.remove(int(UserInput[k]))
            f = f + 1
        f = f - g
        print(str(f) + " numbers are correct, but not in the right spot.")
      else:
        print("Congrualations, you cracked the code!")
        break
    i = i - 1
    print(str(i) + " chances left.")
    if i == 0 :
      print ("Game over")
      break
  cont = int(input("Do you want to play again? (1 = yes or 0 = no): "))
  if cont == 1:
    print("New game:")
  else:
    break
