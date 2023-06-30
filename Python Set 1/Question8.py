# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

def factorial(num) :
    ans = 1
    for i in range(2,num + 1) :
        ans *= i
    return ans


num = 5
ans = factorial(num)

print("factoria of",num,"is :",ans)