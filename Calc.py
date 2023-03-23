def addition(x, y):  # adding two numbers
    add = x + y
    return add


def subtraction(x, y):  # subtracting two numbers
    sub = x - y
    return sub


def multiplication(x, y):  # multiplication of two numbers
    multi = x * y
    return multi


def division(x, y):  # division of two numbers
    div = x / y
    return div


# main program
num1 = int(input("Enter First number:"))  # input1
num2 = int(input("Enter Second number:"))  # input2
op = input('''
1 ----- ADD 
2 ----- SUB
3 ----- MULTI
4 ----- DIV
Enter operation : ''')
# operators for choosing
if op == '1':
    print(f'Addition of numbers {num1} and {num2} is {addition(num1, num2)}')
elif op == '2':
    print(f'Subtraction of numbers {num1} and {num2} is {subtraction(num1, num2)}')
elif op == '3':
    print(f'Multiplication of numbers {num1} and {num2} is {multiplication(num1, num2)}')
elif op == '4':
    print(f'Division of numbers {num1} and {num2} is {division(num1, num2)}')
else:
    print("Enter correct operator")