import re

def replace(user_input, findValue, stopValue):
    if findValue in user_input:
        nav_start = user_input.find(findValue)
        nav_end = user_input.find(stopValue)
        user_input = user_input.replace(user_input[nav_start:nav_end], "ir ")
    return user_input

user_input = str(input("Please, enter phrase: "))
# print(user_input)
sub_str = "slikts"
power = "nav"

if sub_str in user_input and (user_input.find(power)==-1 or user_input.find(power)>user_input.find(sub_str)):
    adapted_input = user_input.replace(sub_str, "labs")
    print (user_input, "->", adapted_input)
elif sub_str in user_input and user_input.find(power)< user_input.find(sub_str):
    adapted_input = user_input.replace(sub_str, "labs")
    adapted_input = replace(adapted_input,power, "labs")
    print (user_input, "->", adapted_input)
else:
    print(user_input + "->" + user_input)


# Uzrakstīt programmu teksta pārveidošanai

# Saglabā lietotāja ievadu

# Izdrukā ievadīto tekstu bez izmaiņām

# Izņēmums: ja ievadā ir vārdi nav .... slikts, TAD izvadā nav ... slikts posms jānomaina uz ir labs

# Laiks nav slikts -> Laiks ir labs

# Auto nav jauns -> Auto nav jauns

# Tas biezpiens nav nemaz tik slikts -> Tas biezpiens ir labs 

# Droši vien noderēs find (vai index, vai pat rfind), tāpat arī in operātors var noderēt. Tāpat slice sintakse būs noderīga.

# Ja uzdevums risinās raiti, tad varam uzlabot un meklēt gan nav ... slikts -> ir labs, gan nav ... slikta -> ir laba