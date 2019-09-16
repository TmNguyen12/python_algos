# Count triplets with sum smaller than a given value
# Given an array of distinct integers and a sum value. 
# Find count of triplets with sum smaller than given sum value. 
# Expected Time Complexity is O(n2).

# Examples:

# Input : arr[] = {-2, 0, 1, 3}
#         sum = 2.
# Output : 2
# Explanation :  Below are triplets with sum less than 2
#                (-2, 0, 1) and (-2, 0, 3) 

# Input : arr[] = {5, 1, 3, 4, 7}
#         sum = 12.
# Output : 4
# Explanation :  Below are triplets with sum less than 12
#                (1, 3, 4), (1, 3, 5), (1, 3, 7) and 
#                (1, 4, 5)

input1 = [ -2, 0, 1, 3]
sum1 = 2
# output = 1

input2 = [ 5, 1, 3, 4, 7]
sum2 = 12
# output = 4

# O(n**3)
def countTriplets_bruteForce (input, sum):
  n = len(input)
  count = 0
  for i in range(0, n - 2):
    for j in range(i+1, n - 1):
      for k in range (j + 1, n):
        if (input[i] + input[j] + input[k] < sum):
          count += 1
  print(count)
  return count

countTriplets_bruteForce(input1, sum1)
countTriplets_bruteForce(input2, sum2)

def countTriplets(input, sum):
  n = len(input)
  input.sort()
  count = 0
  for i in range(0, n - 2):
    j = i + 1
    k = n - 1
    while ( j < k ):
      if (input[i] + input[j] + input[k] >= sum):
        k -= 1
      else:
        count += (k - j)
        j += 1
  print(count)

countTriplets(input1, sum1)
countTriplets(input2, sum2)

# To go from O(n^3) to O(n^2) we start by sorting the array
# If it's sorted, if it the sum is too large we can immediately move the last index (k) to the left
# once we find a 3sum that is less than the sum, we'll know that there are the number of counts
# between the J and K indexes
# After that, we move the J index up one and continue. 

