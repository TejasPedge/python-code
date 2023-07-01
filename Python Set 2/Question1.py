### Problem **1: Print the following pattern**

# Write a program to print the following number pattern using a loop.

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# solution 1

bag = ''

for i in range(1, 6) :
    bag = bag + str(i) + ' '
    print(bag)


# solution 2
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()

