# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and 
# for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
# and 7 ouput Jazz 

# Example:

# n = 15,

# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

def fizzbuzzjazz(n):
  hash = {3: 'Fizz', 5: 'Buzz', 7: ''}
  result = []

  for i in range(1, n+1):
    answer = ''
    for key in hash:
      if i % key == 0 and i != 1:
        answer += hash[key]
    if not answer:
      answer = i    
    result.append(answer)
  print(result)
  return result

fizzbuzzjazz(35)


# The other ways to do this are to 
# 1) Iterate through with conditionals and append to a list
# 2) String concatenate with a bunch of if\'s'
# 3) Hash table - This way you can add/delete mappings to/from to the hash table and not worry about changing the code.

