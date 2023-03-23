def ExceptionHandler():
    # Abnormal Termination handled from try, except and else
    print("Exception with try ,except and else")
    print('One')
    print('Two')
    try:
        print(10 / 0)  # ZeroDivisionError
    except ZeroDivisionError:
        print("Exception Handled")
    else:  # if exception occurs this code will not run :
        print('Four')
        print('Five')
    print()


def ExceptionTry():
    print("Exception with only try and except")
    print("One")
    print("Two")
    try:
        print(10 / 0)
    except ZeroDivisionError:  # ZeroDivisionError
        print("Exception Handled")  # Exception handled
    print("Four")  # this code will run after the exception is handled
    print("Five")
    print()


def AbnormalTermination():
    # Abnormal Termination after ZeroDivisionError:
    print("ZeroDivisionError")
    print('One')
    print('Two')
    print(10 / 0)  # ZeroDivisionError
    print('Four')  # Code will not run after error
    print('Five')
    print()


ExceptionHandler()
ExceptionTry()
AbnormalTermination()
