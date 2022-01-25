""" multiple lines of comments

print('apple\t$1.99 per lb')

# Single comment

multiple lines of comments
hello


# Example 1: Add two numbers
number1 = 20
number2 = 30
addition = number1 + number2
print('The sum is: ', addition)

# Example 2: Using input() function to collect a message from the keyboard
msa = input('Enter a message: ')
print(msa)

# Example 3: Casting - convert from one data type into another
number3 = input('Enter a number: ')
number3 = int(number3)
doubleNum3 = number3*2
print('The number is double to: ', doubleNum3)

# Example 4: Ask the user to enter the height and width of a right triangle as a float value. Calculate the hyp using python math operators and display the result.
# hyp = (x^2+y^2)^0.5
h = float(input('Enter the height: '))
w = float(input('Enter the width: '))
hyp = (h**2+w**2)**0.5  # double astericks are for raising it to an exponent
hyp = int(hyp)
print('A triangle with sides: ', h , ' and ', w, 'has a hypotenus of ', hyp)

# Example 5: Concatenate strings using %s
lastName = "Roy"
firstName = "Puja"
PhoneNumber = '347-712-7519'
num = 2
message = 'The first name is: %s \n The last name is: %s \n The number is: %s'
print(message %(firstName, lastName,num))
print('The first name is: ' + firstName + ' ' +str(num))


# Example 6: split() method for strings
a = "Hello World! Welcome! to! Python"
print(a)
print(a.split("!", 2))

# Example 7: find() method
b = "Hello World"
index = b.find('o')
print('The index for letter o is: ', index)
index1 = b.find('o', 5)
print('The index for letter o after index 5 is: ', index1)

# Example 8: in or not in operator
msg = "Hello World"
answer = 'e' not in msg
print('Is character e in the string?', answer)

# Example 9: Concatenate strings using + operator
a = "apple"
b = " , "
c = "grapes"
fruits = a + b + c
print(fruits)

# Example 10: format() method strings
age = 36
txt = "My name is John, and  I am {}" # In Python, u have to put curly brackets for printing a variable's output
nameAge = txt.format(age)
print(nameAge)
"""

print('ACTIVITY 1')
name = input('Enter a name: ')
number = input('Enter number 1: ')
number = int(number)
number2 = input('Enter number 2: ')
number2 = int(number2)

print('Welcome to Python programming ', name)

sum = number + number2
difference = number - number2
product = number * number2
quotient = number / number2
remainder = number % number2

print('The sum of', number, 'and' , number2  , 'is' , sum)
print('The difference of', number, 'and', number2 , 'is' , difference)
print('The product of', number, 'and' , number2  , 'is' , product)
print('The quotient of', number, 'and' , number2  , 'is' , quotient)
print('The remainder of', number, 'and' , number2  , 'is' , remainder)
