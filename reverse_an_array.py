# Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), 
# reverse the string in a way that special characters are not affected.

# Examples:

# Input:   str = "a,b$c"
# Output:  str = "c,b$a"
# Note that $ and , are not moved anywhere.  
# Only subsequence "abc" is reversed

# Input:   str = "Ab,c,de!$"
# Output:  str = "ed,c,bA!$

import string
import collections 

def reverse_an_array(inputString):
  dict_lower = dict.fromkeys(string.ascii_lowercase, 0)
  dict_upper = dict.fromkeys(string.ascii_uppercase, 0)
  alphabet = list(dict_lower.keys()) + list(dict_upper.keys())

  dinput = collections.deque()
  result_list = []
  for l in inputString:
    if l in alphabet:
      dinput.appendleft(l)
  for idx, l in enumerate(inputString):
    if l in dict_lower.keys() or l in dict_upper.keys():
      result_list.append(dinput.popleft())
    else:
      result_list.append(inputString[idx])
  print("".join(result_list))
  # return result_list.join()

input_string = "Ab,c,de!$"
# reverse_an_array(input_string)
# Output:  str = "ed,c,bA!$

def betterReverse(inputString):
  wordList = list(inputString)
  start = 0
  end = len(wordList) - 1
  while start < end:
    # ignore special characters
    if not wordList[start].isalpha():
      start += 1
    elif not wordList[end].isalpha():
      end -= 1
    else:
      wordList[start], wordList[end] = wordList[end], wordList[start]
      start +=1
      end -= 1
  print("".join(wordList))

betterReverse(input_string)
# Output:  str = "ed,c,bA!$
