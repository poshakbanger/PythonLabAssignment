file = open("NewFile.txt", 'w')
# this line will be written in the new file.
writing_file = "This is the content which is written on the file" \
               "\nHello Bootstrap"
writeFile = file.write(writing_file)  # to write in the file
file.close()  # closing file

# opening file and reading file in python:
file = open("NewFile.txt", "r")
print(file.read())  # reading all the lines of the file
file.close()  # closing file
print()
file = open("NewFile.txt", "r")
print(file.readlines())  # printing lines as list
file.close()  # closing file
print()
file = open("NewFile.txt", "r")
print(file.readline())  # printing only first line - ending the pointer at the end of the 1st line after reading
print(file.readline(5))  # giving the index to print the line
file.close()  # closing file

# finding the length of the text file (total characters)
file = open("NewFile.txt", 'r')
print(len(file.read()))  # calculating the length of the text file "characters in file"
file.close()  # closing file

# finding the length of the text file (total lines in the file)
file = open("NewFile.txt", 'r')
print(len(file.readlines()))  # calculating the length of the text file "lines in file"
file.close()  # closing file