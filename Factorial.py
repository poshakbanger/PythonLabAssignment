def factorial(num):  # factorial of number
    if num == 0:  # fact of 0 is 1.
        return 1
    else:  # fact of other numbers is calculated here
        fact = 1
        while num > 0:
            fact *= num
            num -= 1
        return fact

number = int(input("Enter the number : "))
print("factorial of the number is :", factorial(number))