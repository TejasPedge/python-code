# 1. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"



def Sorting(iterable) :

    n = len(iterable)

    for i in range(n) :
        min_index = i
        for j in range(i+1,n) :
            if iterable[j] < iterable[min_index] :
                min_index = j
        iterable[i],iterable[min_index] = iterable[min_index],iterable[i]
    return iterable

inpt = [64, 25, 12, 22, 11]
ans =  Sorting(inpt)
print(ans)