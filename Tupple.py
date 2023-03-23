# Creating a tuple:
Tuple = ("First index", 1, 2, 3, "akash", True, False, "Last index")

# Functions in tuple:
print("Length of tuple", len(Tuple))  # length of tuple
print("Backward indexing : ", Tuple[-1])  # Backward indexing getting element
print("Forward indexing : ", Tuple[0])  # Forward indexing getting element
print("Slicing in tuple using forward indexing", Tuple[0:2])  # slicing in tuple
print("Printing tuple", Tuple)  # printing tuple

New_Tuple = (1, 2, 3, 4)  # New Tuple
List = [New_Tuple, 1, 2, 34]  # Creating a nested tuple in list
print("nested tuple in list:", List)  # printing tuple in list

# converting tuple into list for mutations
List1 = list(New_Tuple)
print("Changing tuple into list", List1)  # converting tuple into list
List1[1] = "akash"  # changing value
print("After changing value : ", List1)

# appending in tuple by changing tuple into list:
List1.append("New element")
New_Tuple = tuple(List1)
print("After appending in tuple : ", New_Tuple)