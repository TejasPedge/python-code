# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."


inpt = "madam"

str2 = inpt[::-1]

if(inpt == str2) :
    print(f"the word {inpt} is a palindrome")

