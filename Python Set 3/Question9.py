

# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, 
# handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."
import logging

def divide(num1,num2) :

    try :
        return num1/num2
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except TypeError:
        return "Invalid input. Both numbers must be numeric."



print(divide(10,0))

