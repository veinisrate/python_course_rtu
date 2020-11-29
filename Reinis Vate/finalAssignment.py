from helper import inputCharacter, printHangman, cleanPunctuation
import re
import requests
import os
import random

word = str(input('Please enter phrase or word or select \'return\' to generate one: '))
if word=='':
    url = 'https://raw.githubusercontent.com/ValRCS/Python_RTU_08_20/master/data/veidenbaums.txt'
    r = requests.get(url)

    response = re.sub('  +', ' ',  r.text.replace('\n'," "))
    wordList = cleanPunctuation(response).split(' ')
    word=''
    while len(word)<=3:
        word = wordList[random.randrange(0,len(wordList)-1)]
        print(word)

mine_field = ""
accentedCharacters = "ĀČĒĢĪĶĻŅŠŪŽāčēģīķļņšūž"
mine_field = re.sub('[A-Za-z0-9'+ accentedCharacters +']', "*", word) 

attempt = 0
usedCharacters = []

solved = False
while(solved==False and attempt<8):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(printHangman((attempt)))
    print(", ".join(usedCharacters))
    print(mine_field)  
    guess = inputCharacter(f"Input Your guess({attempt}): ").lower()
    if guess not in usedCharacters:
        for c in word:
            if guess==c.lower() and guess not in usedCharacters:
                for index, char in enumerate(word):
                    if char.lower()==c.lower():
                        mine_field = mine_field[:index] + char + mine_field[index+1:]
                attempt-=1
                break
        usedCharacters.append(guess)
    else:
        attempt-=1
    attempt+=1
    if mine_field==word:
        print (f'Congratulations You\'ve solved word: {word}')
        solved=True
    elif attempt>=8:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(printHangman(attempt))
        print(f'Phrase was: "{word}" Sorry,\nYou used letters- "{", ".join(usedCharacters)}" \nBetter luck next time')
