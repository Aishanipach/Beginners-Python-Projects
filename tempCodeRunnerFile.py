def quicksort(arr, lb, ub):
    if (lb < ub):
        loc = partition(arr,lb,ub)
        Quicksort(arr,lb,loc-1)
        Quicksort(arr,loc+1,ub)
def partition(arr, lb, ub):
    pivot = arr[ub]
    i = lb - 1
    for j in range(lb, ub):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[ub] = arr[ub], arr[i + 1]
    return i + 1