mutipleList = []
for i in range (1,1001):
    if (i % 3 == 0) or (i%5 == 0):
        mutipleList.append(i)

print(mutipleList)

sum = 0
for x in mutipleList:
    sum += x

print(sum)