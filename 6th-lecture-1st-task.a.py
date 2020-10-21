number=""
total=0
input_count = 0
while number!='q':
    number = input("Enter float number: ")
    if number!='q':
        input_count=input_count+1
        total+=float(number)
        average = total/input_count
        print(f"{average=}")
# 1.a Vidējā vērtība
# Uzrakstīt programmu, kas liek lietotājam ievadīt skaitļus(float).
# Programma pēc katra ievada rāda visu ievadīto skaitļu vidējo vērtību.
# PS. 1a var iztikt bez lists