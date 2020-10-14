from helper import inputNumber

number: int = inputNumber("input number: ")

prime: bool = True

for i in range(1,int(number**0.5)+1):
    if i!=1 and i!=number:
        if number%i==0:
            prime=False
            break
if prime == False:
    print("Number is NOT prime")
else:
    print("Number is PRIME")