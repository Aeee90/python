#!/bin/python3

import sys


q = int(input().strip())
costs = []
for a0 in range(q):
    n,m,x,y = input().strip().split(' ')
    n,m,x,y = [int(n),int(m),int(x),int(y)]

    list = [];
    for a1 in range(m):
        city_1,city_2 = input().strip().split(' ')
        city = set([int(city_1),int(city_2)])

        check = True
        for i in range(len(list)):
            if len(list[i].intersection(city)) > 0:
                list[i] = list[i].union(city)
                check = False

        if check:
            list.append(city)

    if x < y:
        costs.append(x*n)

    else:
        sum = 0
        for data in list:
            sum += (len(data) -1)*y
            sum += x
            sum += x*(n-len(data))
            costs.append(sum)

    if m is 0:
        costs.append(n*x)

for result in costs:
    print(result)