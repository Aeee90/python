n = 100
n += 1
print(2*sum([i*j for i in range(1, n) for j in range(i+1, n) ]))
