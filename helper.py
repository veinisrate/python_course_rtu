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
       print("Not an integer! Try again.")
       continue
    else:
       return userInput