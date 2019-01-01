capacities = [14, 35, 86, 58, 25, 62]
bottles = [6, 34, 27, 38, 9, 60]
fromId = [1, 2, 4, 5, 3, 3, 1, 0]
toId = [0, 1, 2, 4, 2, 5, 3, 1]

for i in range(len(fromId)):
    moveQuantity = min(capacities[toId[i]] - bottles[toId[i]], bottles[fromId[i]])
    bottles[toId[i]] += moveQuantity
    bottles[fromId[i]] -= moveQuantity

print(bottles)