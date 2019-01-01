num = "0123456789"
count = 0
while count < 1000000:
    tempSet = set([])
    for c in num:
        tempSet.add(c)

    if(len(tempSet) == 10):
        count += 1

    num = str(int(num) + 1)
    if len(num) < 10:
        num = "0" + num


print(num)
