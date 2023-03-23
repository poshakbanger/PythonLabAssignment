def palindrome(string):  # checking palindrome
    if string == string[::-1]:  # if string equals reverse string
        print("The given string is palindrome")
    else:
        print("The given string is not palindrome")


# main program
input_string = input("Enter the String : ")  # taking input
palindrome(input_string)