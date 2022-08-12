#Booleans - True and False
x = True
print(x)
print(type(x))

#operators: ==, !=, >, <, >=, <= 
def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    #The US Constitution says you must be at least 35 years old
    return age >= 35
print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))

def is_odd(n):
    return(n%2)==1
print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))

#Combining boolean values using (and, or, not)
def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship run for president in the US?"""
    #The US Constitution says you must be a natural born citizen *and* be at least 35 years old
    return is_natural_born_citizen and (age>=35)

print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

#Order- and is evaluated before or
True or True and False

# #Using parentheses to make codes clear (use ctrl/)
# prepared_for_weather = have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday
# prepared_for_weather = (
#     have_umbrella
#     or ((rain_level < 5) and have_hood)
#     or (not (rain_level > 0 and is_workday))
# )

#Conditionals: if, elif, else
def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen")
inspect(0)
inspect(-15)

def f(x):
    if x>0:
        print("Only printed when x is positive; x=", x)
        print("Also only printed when x is positive; x=", x)
    print("Always printed, regardless of x's value; x=", x)
f(1); f(0)

#Boolean conversion: bool()
print(bool(1))
print(bool(0))
print(bool("Ray")) 
print(bool(""))

if 0:
    print(0)
elif("spam"):
    print("spam")


#In the cell below, define a function called sign which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.
def sign(x):
    if x>0:
        return 1
    elif x==0:
        return 0
    else:
        return -1

#Example questions from exercise
#Modify the definition in the cell below to correct the grammar of our print statement. (If there's only one candy, we should use the singular "candy" instead of the plural "candies")
def to_smash(total_candies):
    if total_candies == 1:
        print("Splitting 1 candy")
    else:
        print("Splitting", total_candies, "candies")
#Here's a slightly more succinct solution using a conditional expression:
def to_smash(total_candies):
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
