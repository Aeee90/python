import operator as op
import functools as fu
numbers = [1000,999,998,997,996,995]
temp = min(numbers)
print(fu.reduce(op.mul, numbers)*(temp+1)//temp)
