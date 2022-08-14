#Loops: way to repeatedly execute some code
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') #print all on same line

multilplicands = (2,2,2,3,3,5)
product = 1
for mult in multilplicands:
    product = product * mult
product

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
#print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')

#range()
for i in range(5):
    print("Doing important work. i=", i)

#while loops
i = 0
while i < 10: #arg of while statement is boolean, executed until FALSE
    print(i, end=' ')
    i += 1 #increase the value of i by 1

#List comprehensions
squares = [n**2 for n in range(10)]
squares

squares = []
for n in range(10):
    squares.append(n**2)
squares

short_planets = [planet for planet in planets if len(planet)<6]
short_planets

#str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets

#making it look better
[
    planet.upper() + '!'
    for planet in planets
    if len(planet) < 6
]

[32 for planet in planets] #repeats 32 to the number of planets in the list

def count_negative(nums):
    """Return the number of negative numbers in the given list.
    
    >>>count_negatives([-5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
        return n_negative

#to put the code above simple
def count_negatives(nums):
    return len([num for num in nums if num < 0])

#using booleans for the code above, to make it even simpler
def count_negatives(nums):
    return sum([num < 0 for num in nums])

#Readability counts. Explicit is better than implicit.

#Exercises
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0 :
            return True
            #The list has exhausted without finding a lucky number
    return False

def has_lucky_number(nums):
    return any([num % 7 == 0 for num in nums])




