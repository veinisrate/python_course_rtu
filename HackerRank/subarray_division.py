def birthday(s, d, m ):
    options = 0
    for id in enumerate(s):
        if id[0]+m<=len(s):
            calc = sum(s[id[0]:id[0]+m])
            if calc==d:
                options = options + 1
    return options

s = [1, 2, 1, 3, 2]
d = 3
m = 2
result = birthday(s, d, m)
print(result)