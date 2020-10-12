import datetime
from helper import inputNumber

vards = input("Jusu vārds: ")
vecums = inputNumber(str(f"Jusu vecums, {vards}: "))
print(f"Jums būs 100 pēc {100-vecums} gada")
print(f"Jums būs 100 gadi {datetime.datetime.now().year+100-vecums} gadā")
