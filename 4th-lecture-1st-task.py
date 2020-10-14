num = 1
end = 100
while num <= end:
    if num%5==0 and num%7==0:
        print("FizzBuzz", end="")
    elif num%5==0:
        print("Fizz", end="")
    elif num%7==0:
        print("Buzz", end="")
    else:
        print(str(num), end="")
    if num!=end:
        print(",", end="")
    num+=1