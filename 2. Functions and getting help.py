#Getting help
help(round)
help(print)

#Defining funtions
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5 ,6, 7),
)

#Docstrings
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers among a, b and c.
    >>> least_difference(1,5,-5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
help(least_difference)

#Functions that don't return
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5 ,6, 7),
)

#Default arguments
print(1,2,3, sep='<') #in this case, sep= can specify the string in between our printed arguments

def greet(who="Ray"):
    print("Hello,", who)
greet()
greet(who="Kaggle")
greet("world")

#Functions applied to functions
def mult_by_five(x):
    return 5*x
def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)
def squared_call(fn, arg):
    """Call fn on the result of calling fn of arg"""
    return fn(fn(arg))
print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n', #'\n' is the newline character - it starts a new line
)

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x%5
print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5',
    max(100, 51, 14, key=mod_5),
    sep = '\n',
)