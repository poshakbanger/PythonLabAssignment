# Creating a list
List = [1, 2, 33, 4, 5, 6, 7, 8, 9, 10]
#       0  1  2  3  4  5  6  7  8  9  Forward indexing
#     -10 -9 -8 -7 -6 -5 -4 -3 -2 -1  Backward indexing

print("Length of list:", len(List))  # Length of List
print("Accessing item from list:", List[0])  # Accessing element by index

List.remove(2)  # removing "2" from the list
print("After removing element '2':", List)

List.append(999)  # appending '999' in the list
print("After appending '999'", List)

List.pop()  # popping out last element from the list
print("Popping last element from the list: ", List)

sorted_list = List.copy()  # copying list

sorted_list.sort()  # sorting list using sort function
print(sorted_list)  # sorted list

print("Forward slicing", List[0:3:1])  # Forward slicing
print("Backward Slicing", List[-1::-1])  # Backward slicing