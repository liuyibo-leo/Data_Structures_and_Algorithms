def MergeSort(arr):
    n = len(arr)
    _mergeSort(arr, 0, n-1)

def _mergeSort(arr, begin, end):

    if begin >= end:
        return

    mid = (end-1) // 2 #(end - 1) means to get the actual position.
    _mergeSort(arr, 1, mid) #
    _mergeSort(arr, mid+1, end)
    Merge(arr, 1, mid, end)

def Merge(arr, begin, mid, end):

    arr_Copy = arr

    i, j = begin, mid+1

    for k in range(begin, end+1): #end+1 means to get the actual position
        if i > mid:
            arr[k] = arr_Copy[j - 1]
            j += 1
        elif j > end:
            arr[k] = arr_Copy[i - 1]
            i += 1
        # compare each of the two sets (divided by 2, to find the mid) of the array one position by position of the two sub-arrays
        elif arr_Copy[i - 1] < arr_Copy[j - 1]:
            arr[k] = arr_Copy[i - 1]
            i += 1
        else:
            arr[k] = arr_Copy[j - 1]
            j += 1



