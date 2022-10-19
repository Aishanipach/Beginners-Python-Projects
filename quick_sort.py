# function to find the partition position
def partition(arr, lb, hb):

  # choose the rbtmost element as pivot
  pivot = arr[hb]

  # pointer for greater element
  i = lb - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(lb, hb):
    if arr[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (arr[i], arr[j]) = (arr[j], arr[i])

  # swap the pivot element with the greater element specified by i
  (arr[i + 1], arr[hb]) = (arr[hb], arr[i + 1])

  # return the position from where partition is done
  return i + 1

def quickSort(arr,lb,ub):
    if (lb < ub):
        loc = partition(arr,lb,ub)
        quickSort(arr,lb,loc-1)
        quickSort(arr,loc+1,ub)

data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array: ")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

#Time complexity: O(n*log n)
#Space complexity: O(log n)