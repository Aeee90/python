import copy

friends = ["NYNNN",
           "YNYNN",
           "NYNYN",
           "NNYNY",
           "NNNYN"]

network = {}
for i in range(len(friends)):
    temp = set()
    for j in range(len(friends[i])):
        if friends[i][j] == "Y" :
            temp.add(j)

    network[i] = temp

print(network)
max = 0
for i,j in network.items():
    temp = copy.deepcopy(j)
    for k in j:
        print(network[k])
        temp |= network[k]

    if len(temp) > max:
        max = len(temp)

print(max - 1)