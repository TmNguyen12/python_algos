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
* python uses "and" and "or" instead of "&&" and "||"




#### Links 
- https://medium.com/@Ljyockey/python-syntax-a-beginners-guide-for-javascript-developers-5bdc1066ac4c

## List comprehension 
- `[expression for item in list]`
- `[expression for item in list if conditional]
```

```


## `builtin methods used`
- range(start, stop, step)
- 

### `string`
- lower() 
  - lowercases a string
  - `str.lower()`
- f"here {interopla} now" 
  - is a way to do string interopolation similar to `` in javascript 
- `print("its fleece was white as {}.".format('snow'))` => its fleece was white as snow.
- x.isalpha()
  - returns true if x is an alphanumeric character
- word.replace('.', '[.]')
  - if word = '9.2', then it'll equal '9[.]2'
- list('hello')
  - ['h', 'e', 'l', 'l', 'o']

### `integer`
- int(7.7) = 7 
- 3/2 = 1.5 (3.x)
- 3//2 = 1 (integer output use double slash )
- 1/2 = 0 
- 3/2.0 = 1.5 

### `list`
- row[~i] = row[-i-1] = row[len(row) - 1 - i]
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
- array.sort()
  - mutates the list
- for idx, value in enumerate(arrayList)
  - how to iterate through a list with index and value
- arr.index('a')
  - returns the index the item is at or raises a ValueError if nothing is found 
- arr.find('a')
  - same as .index but returns -1 instead of a ValueError when something isn't found 
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
- turning a list into a string 
```python
  myList = ['a','b','c','d']
  word = ''.join(myList)
  print(word) #abcd
  comma = ', '.join(myList)
  print(comma) # a, b, c, d
```

### `dict`
- if 'you' in dict: 
  - you can check to see if a key exists 
- iterate through a dict
  - key value pairs 
    - `for key, value in myDict.items()`
  - keys only
    - `for key in myDict`
  - values only
    - `for value in myDict.values()`

### `set`
- set()
- set([list])
- set{'a','b','s'}
### Links 
https://www.pythoncentral.io/python-null-equivalent-none/
