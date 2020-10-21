number_list = []
number = ''
while number!='q':
    number = input("Enter float number or q to quit: ")
    if number!='q':
        number_list.append(float(number))
        number_list.sort()
        print(f"top3= {number_list[-3:]} bottom3={number_list[:3]}")
        print(f"average:{sum(number_list)/len(number_list)}")

# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.
