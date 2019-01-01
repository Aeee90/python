first = ['fishing', 'gardening', 'swimming', 'fishing']
second = ['gardening', 'fishing', 'fishing', 'swimming']

temp = first + second
result = {}
for i in temp:
    result[i] = 1 if result.get(i) is None else result.get(i)+1

print(max(result.values()))