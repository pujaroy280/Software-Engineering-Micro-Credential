"""
Week 4 - Activity 4, 5 and 6
Puja Roy
Functions
"""
"""
import math, random
# Example 1: Find the circumference of a circle given the radius

radius = int(input("Enter a radius: "))
c = 2*radius*math.pi
c = round(c,2)
print("The circumference with radius %s is %s" %(radius,c))

# Example 2: Find the area of a circle
print("\n -------- Example 2 --------\n")
area = math.pow(radius,2)*math.pi
area = math.ceil(area)

print("The area with radius %s is %s" %(radius,area))


# DEFINED FUNCTION
# Example 3: Create a function, no argument, no return value

def hello():
    print("Hello from a function")

hello()

#Example 4:
print("\n -------- Example 4 --------\n")
def name(fname):
    print('My name is: ', fname)

name("Email")
name("Peter")
user = input("Enter a name: ")
name(user)

# Example 5: Function with default parameter value
print("\n -------- Example 5 --------\n")
def country(c = "Norway"):
    print("I am from ", c)

# Example 6: Function with two parameters and a returning value
print("\n -------- Example 6 --------\n")
def sum(num1, num2):
    total = num1+num2
    return total

def number():
    n1 = int(input('Enter num1: '))
    n2 = int(input('Enter num2: '))
    t = sum(n1,n2)
    print("The sum of %s and %s is %s" %(n1,n2, t))

number()

country()
country("USA")


# Example 7: Function with arbitrary arguments
print("\n -------- Example 7 --------\n")
def children(*kids):
    n = len(kids)
   # print("The second kid is: %s among %s children" % (kids[1],n))
     print(n)
     
names = children['Emil','Tobias','Linus','Peter']
names1 = children['Emil','Tobias']
print(children(names, names1))


import math, random
# Example 8: Boolean Functions
print("\n -------- Example 8 --------\n")
# Write a function that will evaluate if two numbers are divisible by each other

def is_divisible(x,y):
    if x%y == 0 or y%x==0:
        return True
    else:
        return False
    
print(is_divisible(8,3))
print(is_divisible(10,5))
print(is_divisible(5,10))

# Example 9: Random Number
print("random()", random.random())
print("using uniform()", random.uniform(0,10))
print("using randint()", random.randint(0,10))
print("using randrange()", random.randrange(0,101,5))

# Generate more than one random number
for x in range(10):
    print(random.randint(1,101))

"""

# Activity 4
print("\n -------- ACTIVITY 4 --------\n")
#function for caluculating volume of cylinder
def volumeCylinder(h,r):
    return round(r*r*PI*h,2)  # In order to round the value use round(variable,2) so that the value will be rounded to 2 decimal points.
#entering the values from user
r=int(input("Enter a radius: "))
h=int(input("Enter the height: "))
PI=3.141592653589793  # Value of PI
print("The volume with radius" ,r, "and height",h,"is",volumeCylinder(h,r)) # printing the volume of the cylinder


# Activity 5
print("\n -------- ACTIVITY 5 --------\n")
import math
import random

def roll(num):
    for i in range(0,num):
        print("Roll",i,"=",random.randint(1,6))

num = int(input("Enter the number of times you want to roll: "))
roll(num)

"""
import math
import random

r=int(input("How many times do you want to roll?: "))
for r in range(1,4):
    print("Roll",r, "=",random.randint(1,6))

"""
# Activity 6
print("\n -------- ACTIVITY 6 --------\n")
word = input('Enter a word: ')
def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse(word))
