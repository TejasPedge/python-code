# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."


my_list = list(range(1,11));

print(my_list)

my_list.append(2)

print("Added List :",my_list)

my_list.remove(5)

print("removed List :",my_list)

my_list.sort();

print("Sorted List :",my_list)



