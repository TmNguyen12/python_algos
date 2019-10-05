# Convert array into Zig-Zag fashion
# Given an array of DISTINCT elements, rearrange the elements of array in zig-zag 
# fashion in O(n) time. The converted array should be in form a < b > c < d > e < f.

# Example: 
# Input:  arr[] = {4, 3, 7, 8, 6, 2, 1}
# Output: arr[] = {3, 7, 4, 8, 2, 6, 1}

# Input:  arr[] =  {1, 4, 3, 2}
# Output: arr[] =  {1, 4, 2, 3}

arr = [4, 3, 7, 8, 6, 2, 1]
result = [3, 7, 4, 8, 2, 6, 1]
# odd means greater than
# even means less than 
def zigZagSort(arr):
  for i in range(len(arr)-1):
    if i == 0 and arr[i] > arr[i+1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]
    elif i % 2 != 0:
      if arr[i] < arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
    else:
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
  print(arr)
  return arr 

zigZagSort(arr)
# Time Complexity: O(n)
# Space Complexity: O(1)



