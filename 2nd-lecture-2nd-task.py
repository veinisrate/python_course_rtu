from helper import inputFloat

height = inputFloat("Height: ")
width = inputFloat("Width: ")
length = inputFloat("Length: ")
print(f"Room volume is: {round(height*width*length,2)}")