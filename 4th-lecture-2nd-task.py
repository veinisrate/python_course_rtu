from helper import inputNumber
height: int = inputNumber('enter height: ')
for line in range(height):
    for space in range(height-line):
        print(" ", end="")
    for star in range(2*line+1):
        print("*", end="")
    print("")
print('-'*int(2*height+1))
for line in range(height):
    print(" " * (height-line), end="")
    print("*" * int(2*line+1))
