import operator  # importing operator
from functools import reduce # importing reduce
from itertools import accumulate # importing accumulate


def sumOfList(a, b):
    sum = a + b  # sum of a and b
    return sum


List = [1, 2, 3, 4, 5, 6]
a = (reduce(sumOfList, List))  # returns last value of the function
print(a)

b = list(accumulate(List, operator.add))  # returns result after every operation
print(b)