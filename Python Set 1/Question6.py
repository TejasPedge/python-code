# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"



def count_vowels(string) : 
    count = 0
    vowels = "aeiouAEIOU" 

    for char in string :
        if (char in vowels) :
            count += 1

    return count

str = "hello"
count = count_vowels(str)
print("Vowels count :",count)