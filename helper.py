def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput

def inputFloat(message):
  while True:
    try:
       userInput = float(input(message))       
    except ValueError:
       print("Not an float! Try again.")
       continue
    else:
       return userInput

def inputCharacter(message):
  while True:
    try:
       userInput = str(input(message))       
    except ValueError:
       print("Not an string! Try again.")
       continue
    else:
       return userInput[0]