# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."


def isPrime(number) : 

    if (number < 2) : 
        return False

    for i in range(2,int((number ** 0.5) + 1)) :
        if(number % i == 0) : 
            return False

    return True


number = 13

if (isPrime(number)) :
    print(number,"is a prime number")
else :
    print(number,"is not a prime number")

