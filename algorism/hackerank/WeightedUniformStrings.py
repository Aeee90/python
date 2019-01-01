#!/bin/python3

import sys

s = input().strip()
n = int(input().strip())

def analysisStr(str):
    result = []
    preStack = 0
    preC = None
    w = 0
    for i in range(len(str)):
        w = ord(str[i]) - 96

        if str[i-1] is str[i]:
            w += preStack

        result.append(w)
        preStack = w

    return set(result)

dataSet = analysisStr(s)

x =[]
for a0 in range(n):
    x.append(int(input().strip()))

for i in x:
    result = "No"
    if len(dataSet.intersection([i])) is not 0:
        result = "Yes"
    print(result)