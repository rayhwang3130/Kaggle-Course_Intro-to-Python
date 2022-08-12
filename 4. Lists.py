#Lists
primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K']
]
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]
my_favorite_things = [32, 'raindrops on roses', help]
print(my_favorite_things)

#Indexing: index starts from 0
planets[0]
planets[1]
planets[-1]
planets[-2]

#Slicing
planets[0:3]
planets[3:]
planets[1:-1] #All the planets except the first and last
planets[-3:] #The last 3 planets

#Changing lists
planets[3]="Malacandra"
planets
planets[:3]=["Mur", "Vee", "Ur"]
print(planets)
planets[:4]=["Mercury", "Venus", "Earth", "Mars"] #Giving them back their own names

#List functions
len(planets) #len gives the length of the list
sorted(planets) #returns sorted ver. of list

primes = [2, 3, 5, 7]
sum(primes)
max(primes)
min(primes)

#Objects
x = 12
#x is a real number, so its imaginary part is 0
print(x.imag)
#Making a complex number
c = 12 + 3j
print(c.imag)

x.bit_length()
help(x.bit_length)

#List methods
#Adding Pluto to the planets list
planets.append('Pluto')
planets
planets.pop()
planets
planets.index('Earth')
planets.index('Pluto')

#Searching lists
#Is Earth a planet?
"Earth" in planets
#Is Calbefraques a planet?
"Calbefraques" in planets

#Tuples - use parentheses, cannot be modified
t = (1,2,3)
t = 1,2,3
#used for functions that have multiple return values
x = 0.125
x.as_integer_ratio()
numerator, denominator = x.as_integer_ratio()
print(numerator/denominator)

a = 1
b = 0
a, b = b, a
print(a, b)
