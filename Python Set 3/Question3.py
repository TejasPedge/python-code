# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"


integers = [2, 7, 11, 15]
target = 9

obj = {}

ans =[]

for index,num in enumerate(integers):

    x = target - num
    
    if(x in obj) :
        ans.append(obj[x])
        ans.append(index)

        break
    else :
        obj[num] = index


print(ans)