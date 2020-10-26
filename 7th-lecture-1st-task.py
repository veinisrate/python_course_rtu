# 1. Lielais rezultāts
# Uzrakstiet funkciju add_mult, kurai nepieciešami trīs parametri/argumenti
# Atgriež rezultātu, kas ir 2 mazāko argumentu summa reizināta ar lielāko argumenta vērtību.
# PS Uzskatīsim, ka funkcijai vienmēr tiks padoti skaitliski parametri, varam tipus nepārbaudīt.
# Iespējami dažādi risinājumi, piemēram ar list struktūru varētu būt tīri eleganti.
# Piemērs add_mult(2,5,4) -> atgriezīs (2+4)*5 = 30

def add_mult(x, y, z) -> float:
    mult_list = [x, y, z]
    mult_list.sort()
    x, y, z = mult_list
    return (x+y)*z

print(add_mult(1,2,3))
print(add_mult(3,2,1))
print(add_mult(2,1,3))

print(add_mult(3,3,1))
print(add_mult(3,1,3))
print(add_mult(1,3,3))
