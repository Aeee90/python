#!/bin/python3

import sys

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

def getGCM(a, b):
    if(a < b):
        temp = a
        a = b
        b = temp

    r = int(a % b)

    print("{},{}".format(b, r))
    if r is 0:
        return b
    else:
        return getGCM(b, r)


def getLCM(a, b):
    return a * b / getGCM(a, b)


def getLCMinList(list):
    prev = int(1)
    for i in list:
        prev = getLCM(i, prev)

    return prev


ax = getLCMinList(a)
print(ax)
bx = int(min(b)/ax )
count = 0

for i in range(1,bx+1):
    def aa(i):
        for j in b:
            if j % i != 0:
                return False
        return True


    if aa(i*ax):
        count += 1

print(count)
print("---------------------------------")

getGCM(6,9)