from helper import inputCharacter
import re
player_one_input = str(input('Player one, please, enter text: '))
mine_field = ""
string_to_solve = ""

# for c in player_one_input:
#     if (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
#         mine_field+="*"
#         string_to_solve += c
#     elif (c==" "):
#         mine_field+=" "
#         string_to_solve += c   
  
# Regex way is shorter:
mine_field = re.sub('[A-Za-z0-9]', "*", player_one_input)  
string_to_solve = player_one_input 

print(player_one_input)
print(mine_field)
print(string_to_solve) # in case of regex it's redundant, was necessary for ascii compare though leaving in for test purposes

solved = False
while(solved==False):
    guess = inputCharacter("Input Your guess: ")
    for c in string_to_solve:
        if guess==c:
            for index, char in enumerate(string_to_solve):
                if char==c:
                    mine_field = mine_field[:index] + c + mine_field[index+1:]
    if mine_field==string_to_solve:
        print ("Congračuleišans")
        solved=True
    else:
        print(mine_field)



# Uzrakstīt programmu teksta simbola atpazīšanai

# Lietotājs(pirmais spēlētājs) ievada tekstu.

# Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt

# Lietotājs(tātad otrs spēlētājs) ievada simbolu. 

# Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.

# Kartupeļu lauks -> ********* *****

# ievada a -> *a****** *a***

# Principā tas ir labs iesākums karātavu spēlei.