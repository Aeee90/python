names = []
with open(".//data//names.txt") as f:
    names = list(map(lambda t: t.replace("\"", ""), f.read().split(",")))

names.sort()
num = 64
total = 0
for i in range(len(names)):
    temp = 0
    for j in names[i]:
        temp += ord(j) - num
    total += temp*(i+1)
print(total)