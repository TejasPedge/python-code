# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

def reverse_string(string) : 
    reversed_string = string[::-1]
    
    return reversed_string

string = "Python" 
print("Reversed String",reverse_string(string))