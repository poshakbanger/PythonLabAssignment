x = lambda a: a + 10  # giving only single argument
print("Adding 10 to a : ", x(5))

x = lambda a, b: a * b  # giving two argument a and b
print("Multiplying two numbers", x(4, 5))  # giving the value in function


def double(n):  # function to multiply the number N times
    return lambda a: a * n  # a times n


func = double(2)  # multiplying number 2, a times
print(func(4))  # giving number of times to multiply