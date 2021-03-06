from helper import inputNumber
height: int = inputNumber('enter height: ')
# Standard tree
for line in range(height):
    for space in range(height-line):
        print(" ", end="")
    for star in range(2*line+1):
        print("*", end="")
    print("")
print('-'*int(2*height+1))
# Python like tree
for line in range(height):
    print(" " * (height-line-1), "*" * int(2*line+1))