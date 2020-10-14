from helper import inputNumber

number: int = inputNumber("input number: ")

prime: bool = True

for i in range(1,number):
    if i!=1 and i!=number:
        if number%i==0:
            prime=False
if prime == False:
    print("Number is NOT prime")
else:
    print("Number is PRIME")