from helper import inputNumber, inputFloat
yearCount = inputNumber("What's Your standing in the company in years?")
salary = inputFloat("What's Your salary in Eur?")
bonus=0.15
if yearCount>2:
    print(f"You will receive {salary*bonus*(yearCount-2)} Eur anual bonus")
else: 
    print("Sorry, You do not have dedicated suffienct amount of time to our company!")