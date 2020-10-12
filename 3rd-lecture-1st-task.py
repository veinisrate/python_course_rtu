from helper import inputFloat
bodyTemperature = inputFloat("What's Your body temperature? ")
if bodyTemperature<35:
    print("Nav par aukstu?")
elif bodyTemperature<=37:
    print("Viss kārtībā")
else:
    print("Iespējams drudzis")