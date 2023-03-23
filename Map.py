def double(n):
    return n * 2


numbers = [1, 2, 3, 4]
result = map(double, numbers)  # transforms all the items in list without another iteration
print(list(result))