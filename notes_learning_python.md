# Notes - Learning Python


#### Nuggets 
* Booleans are *capitalized* in Python 
* The convention in Python is to define functions and variables using joined_lower casing (classes use StudlyCaps casing).
* Indent using 2 spaces
* Parentheses are not required for the conditional statements.
* The “print” keyword is used to print to the console.
* To make a single-line comment, use “#”.
* you can do i in str or i in dict to see if an item is in a list or dictionary
* dictionary = hash map or JS object
* list = array 
* any quotes inside of an outside quotes do not need to be escaped if different quote length (single for double quotes)
* If you can print it, or assign it to a variable, it’s an expression. If you can’t, it’s a statement.
* Keyword arguments are often used for optional parameters 
* 



#### Links 
- https://medium.com/@Ljyockey/python-syntax-a-beginners-guide-for-javascript-developers-5bdc1066ac4c


## `builtin methods used`


### `string`
- lower() 
  - lowercases a string
- f"here {interopla} now" 
  - is a way to do string interopolation similar to `` in javascript 
- `print("its fleece was white as {}.".format('snow'))` => its fleece was white as snow.
- 

### `integer`
- int(7.7) = 7 

### `list`
- len(i)
  - returns length of list
- .append(i)
  - pushes something onto the back of the list 
- arr.extend(arr2)
  - add to lists together 
- reverse(arr)
  - return an enumeral that is the list reversed (also works with strings)
- max()
- min()
```python
def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    return sum

# using max(arg1, arg2, *args, key)
print('Maximum is:', max(100, 321, 267, 59, 40, key=sumDigit))
```

### `dict`
- if 'you' in dict: 
  - you can check to see if a key exists 
- 

