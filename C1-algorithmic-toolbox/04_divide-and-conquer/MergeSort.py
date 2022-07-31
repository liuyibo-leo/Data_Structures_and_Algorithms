def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])

    return Merge(left, right)

def Merge(left, right):
    l, r = 0, 0
    result = []

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += list(left[l:]) #if 'l' is greater than the len's range, the 'left[l:]' will return nothing.
    result += list(right[r:]) #if 'r' is greater than the len's range, the 'right[r:]' will return nothing.
    return result

print(mergeSort([8,4,5,7,1,3,6,2]))
