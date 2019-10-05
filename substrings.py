def substring(str):
  res = [str[i:j] for i in range(len(str))
          for j in range(i + 1, len(str)+1) if len(str[i:j]) == 1]
  print(res)
[str[i:j] for i in range(len(S)) for j in range(i+1, len(S)+1) if len(str[i:j]) == 1]

# substring with only one letter 


test_str = 'Geeks'
substring(test_str)


# 01234 

# 01, 02, 03, 04, 05, 06 
