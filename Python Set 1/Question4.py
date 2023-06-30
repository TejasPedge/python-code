# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"


def calculate_average_sum(list) :
    addition = sum(list)
    average = addition / len(list)
    return addition, average

list = [10,20,30,40]
addition, average = calculate_average_sum(list)
print(f"Sum : {addition}", f"Average : {average}")

