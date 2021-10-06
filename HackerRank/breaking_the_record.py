def breakingRecords(scores):
    max = scores[0]
    min = scores[0]
    countMin = 0
    countMax = 0
    for score in scores[1:len(scores)]:
        if score>max:
            max = score
            countMax=countMax+1
        elif score<min:
            min=score
            countMin=countMin+1
    return [countMax, countMin]

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
result = breakingRecords(scores)
print(result)