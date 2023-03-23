List1 = []  # taking an empty list
List2 = [1, 2, 3, 4, 5, 6]  # comparing list
n = int(input("Enter number of elements : "))  # length of list

for i in range(0, n):  # taking input in list1
    item = int(input("Enter Item in list :"))
    List1.append(item)  # adding items in list1

for k in List2:  # for items in list2
    if k in List1:  # if the items are in list1
        ans = "Equal"
    else:
        ans = "Not Equal"

print(ans)