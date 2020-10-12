from helper import inputNumber
a = input('a: ')
b = input('b: ')
c = input('c: ')

if a<b and a<c:
    if b<c: print(f"a {a}, b {b}, c {c}")
    else: print(f"a {a}, c {c}, b {b}")
elif b<a and b<c:
    if a<c: print(f"b {b}, a {a}, c {c}")
    else: print (f"b {b}, c {c}, a {a}")
else c<a and c<b:
    if a<b: print(f"c {c}, a {a}, b {b}")
    else: print (f"c {c}, b {b}, a {a}")

#other option (easier)
sort_list = [a, b, c]
print(sort_list)
sort_list.sort()
print(sort_list)