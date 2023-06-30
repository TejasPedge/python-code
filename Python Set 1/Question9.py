# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

def fibonacci_sequence(num) : 
    sequence = [0, 1]

    for i in range(2,num) :
        next_fib_num = sequence[-1] + sequence[-2]
        sequence.append(next_fib_num)

    return sequence

num = 5
answer = fibonacci_sequence(num)

print(answer)