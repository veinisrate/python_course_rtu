my_sentence = input("Please, enter sentence: ")
my_awkward_sentence=[]
my_sentence = my_sentence.split()
for word in my_sentence:
    my_awkward_sentence.append( word[::-1])

print(f"{' '.join(my_awkward_sentence).capitalize()}")
# 3. Apgrieztie vārdi
# Lietotājs ievada teikumu.
# Izvadam visus teikuma vārdus apgrieztā formā.
# Alus kauss -> Sula ssuak
# PS Te varētu noderēt split un join operācijas.

