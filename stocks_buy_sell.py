# Stock Buy Sell to Maximize Profit
# The cost of a stock on each day is given in an array, 
# find the max profit that you can make by buying and selling in those days. 
# For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit 
# can earned by buying on day 0, selling on day 3. Again buy on day 4 and sell on day 6. 
# If the given array of prices is sorted in decreasing order, then profit cannot be earned 
# at all.

# Buy on day : 0   Sell on day: 3
# Buy on day : 4   Sell on day: 6
# 310 - 100 =  210 
# 695 - 40 = 655 
stocks = [100, 180, 260, 310, 40, 535, 695]
sum = 865 

def buy_sell(info):
  start = None 
  sum = 0

  for i, n in enumerate(info):
    if start is None:
      start = i
    elif n < info[i-1]:
      sum += (info[i-1] - info[start])
      start = i
    elif i == len(info) - 1:
      sum += info[i] - info[start]
  print(sum)
  return sum 

buy_sell(stocks)

