# Write a program to reverse an array or string
# Given an array (or string), the task is to reverse the array/string.

# Examples :

# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}

def reverseString(word):
  start = 0
  end = len(word) - 1
  wordList = list(word)
  while start < end:
    wordList[start], wordList[end] = wordList[end], wordList[start]
    start += 1
    end -= 1
  print("".join(wordList))

reverseString('hello')