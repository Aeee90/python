def isPrimes(self, num):
    primes = [2]
    for i in range(3, num + 1, 2):
        ch = True
        for j in range(3, int(i ** 0.5 + 1)):
            if i % j == 0:
                ch = False
                break

        if ch:
            primes.append(i)
    return primes