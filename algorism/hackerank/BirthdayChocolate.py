n, s = int(input().strip()), list(map(int, input().strip().split(' ')))
d, m = list(map(int, input().strip().split(' ')))
print([ i for i in range(n-m+1) if sum(s[i:i+m]) is d])