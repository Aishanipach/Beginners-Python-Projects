rr,lb,ub):
    if (lb < ub):
        loc = partition(arr,lb,ub)
        Quicksort(arr,lb,loc-1)
        Quicksort(arr,loc+1,ub)