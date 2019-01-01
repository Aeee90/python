num = 600851475143
result = 2
while num%2 == 0:
        num = num//2

for i in range(3, int(num**0.5)+1, 2):
    while num%i is 0:
        result = i
        num = num//i

print(result)