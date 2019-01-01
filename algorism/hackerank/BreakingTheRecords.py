n = int(input());
scores = [int(i) for i in input().split(" ")]

high = 0
highest = scores[0]
low = 0
lowest = scores[0]

for i in scores:
    if highest < i:
        highest = i
        high += 1
    elif lowest > i:
        lowest = i
        low += 1


print("{} {}".format(high, low))