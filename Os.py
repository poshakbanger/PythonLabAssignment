import os

path = "C:/Users/Hp/OneDrive/Desktop/OS.txt"  # path of the file


def file_exists(): # Checks whether the file exists or not at the path given
    print(os.access(path, os.F_OK))


def file_read(): # Checks whether user can read or not
    print(os.access(path, os.R_OK))


def file_write():  # Checks whether there is permission to write or not
    print(os.access(path, os.W_OK))


def path_execution():  # Checks if path can be executed
    print(os.access(path, os.X_OK))


# Gives boolean value as Output
file_write()
file_read()
file_exists()
path_execution()