from helper import inputNumber

begin = int(inputNumber('Enter start number: '))
end = int(inputNumber('Enter finish number: '))

my_list = list(range(begin,end+1))
my_qube_list= [i**3 for i in my_list]
for i in range(len(my_list)):
    print(f"{my_list[i]}^3: {my_qube_list[i]}")
print(f"List^3:{my_qube_list}")

# 2. Kubu tabula
# Lietotājs ievada sākumu (veselu skaitli) un beigu skaitli.
# Izvads ir ievadītie skaitļi un to kubi
# Piemēram: ievads 2 un 5 (divi ievadi)
# Izvads 
# 2 kubā: 8
# 3 kubā: 27
# 4 kubā: 64
# 5 kubā: 125
# Visi kubi: [8,27,64,125]
# PS teoretiski varētu iztikt bez list, bet ar list būs ērtāk