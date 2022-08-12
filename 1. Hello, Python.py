#Example of the SPAM skit

spam_amount = 0 #assigning & creating a variable using = (assignment operator)
print(spam_amount) #the print() function

#Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4
if spam_amount > 0: #colon : creates a code block
    print("But I don't want ANY spam!") #example of a string

viking_song = "Spam" * spam_amount #operator overloading
print(viking_song)

#type() -> what type of thing is it?
type(spam_amount) #int- integer
type(19.95) #float- number with deciamal place

#Arithmetics +-*/
print(5/2); print(6/2) #prints the quotient
print(5//2); print(6//2) #prints the quotient, removes fractional parts
print(5%2) #prints integer remainder
print(2**3) #prints 2 to the power 3 (2^3)

#Example of order of calculation and why using parentheses are important
hat_height_cm = 25
my_height_cm = 190
#How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")
total_height_meters = (hat_height_cm+my_height_cm)/100
print("Height in meters =", total_height_meters)

#min / max
print(min(1,2,3))
print(max(1,2,3))
#abs- absolute value
print(abs(32))
print(abs(-32))
#int / float
print(float(10))
print(int(3.33))
print(int('807')+1)

# Exercise
# Swapping a and b
a = [1,2,3]
b = [3,2,1]
tmp = a
a = b
b = tmp
a, b
#or simply
a, b = b, a
a, b

