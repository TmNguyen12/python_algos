# DI String Match

# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]
 
# Example 1:
Input1 = "IDID"
Output1 = [0,4,1,3,2]

# Example 2:
Input2 = "III"
Output2 = [0,1,2,3]

# Example 3:
Input3 = "DDI"
Output3 = [3,2,0,1]

# The trick here is to go through the input string and add the previous value into the results
# based on what the string is telling you. For example, if you get an I, then you add the previous
# value as the smallest possible thing so that the next one will be larger

def diStringMatch(S):
    highidx = len(S)
    lowidx = 0
    result = []
    for s in S:
        if s == 'I':
            result.append(lowidx)
            lowidx += 1
        else:
            result.append(highidx)
            highidx -= 1
    result.append(highidx)
    print(result)
    return result

diStringMatch(Input1)
diStringMatch(Input2)
diStringMatch(Input3)


