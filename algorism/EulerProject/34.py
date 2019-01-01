import math
factorialMap = [math.factorial(i) for i in range(10)]
print(sum([ i for i in range(10, 10**6) if sum([factorialMap[int(j)] for j in str(i)]) == i]))