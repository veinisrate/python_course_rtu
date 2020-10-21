
number_list = []
number = ''
while number!='q':
    number = input("Enter float number or q to quit: ")
    if number!='q':
        number_list.append(float(number))
        print(number_list)
        print(f"average:{sum(number_list)/len(number_list)}")

# 1.b Programma rāda gan skaitļu vidējo vērtību, gan VISUS ievadītos skaitļus
# PS Iziešana no programmas ir ievadot "q"
