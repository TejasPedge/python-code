### Problem **6: Concatenate two lists in the following order**

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# **Expected output:**

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]


concanated_list = [item1 + item2 for item1 in list1 for item2 in list2]
print(concanated_list)

