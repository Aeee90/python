result =0
for i in range(999, 99, -1):
    for j in range(999, i-1, -1):
        temp = i*j
        if str(temp) == str(temp)[::-1] :
            result = temp if temp > result else result

print(result)