### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:

# str1 = PyNaTive

# **Expected Output**:

# yaivePNT


str1 = "PyNaTive"

lower_case = [char for char in str1 if char.islower()]

upper_case = [char for char in str1 if char.isupper()]

result = ''.join(lower_case + upper_case)

print(result)

