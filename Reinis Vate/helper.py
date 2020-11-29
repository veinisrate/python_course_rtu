import string

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
            if userInput == '':
                raise ValueError
        except ValueError:
            print("Not an string! Try again.")
            continue
        else:
            return userInput[0]


def printHangman(i):

    attempt = {
        0: "\n" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n",
        1: "\n______________" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n",
        2: "\n______________" + "\n|            |" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n",
        3: "\n______________" + "\n|            |" + "\n|           O" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n",
        4: "\n______________" + "\n|            |" + "\n|           O" + "\n|           |" + "\n|" + "\n|" + "\n|_______________________\n",
        5: "\n______________" + "\n|            |" + "\n|           O" + "\n|        ---|" + "\n|" + "\n|" + "\n|_______________________\n",
        6: "\n______________" + "\n|            |" + "\n|           O" + "\n|        ---|---" + "\n|" + "\n|" + "\n|_______________________\n",
        7: "\n______________" + "\n|            |" + "\n|           O" + "\n|        ---|---" + "\n|           /" + "\n|          /" + "\n|_______________________\n",
        8: "\n______________" + "\n|            |" + "\n|           O" + "\n|        ---|---" + "\n|           /\\" + "\n|          /  \\" + "\n|_______________________\n"
    }
    return attempt.get(i)


def cleanPunctuation(inputString):
   for symbol in string.punctuation:
        inputString = inputString.replace(symbol, "")
   return inputString
