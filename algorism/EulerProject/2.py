def fibonacciWhileGenerator(a, b, n):
    n_2, n_1, i = a, b, 0
    yield n_2
    yield n_1
    while i <= n:
        i = n_1 +  n_2
        n_1, n_2 = i, n_1
        yield i


print(sum([ i for i in fibonacciWhileGenerator(1, 2, 4000000) if i%2 is 0]))