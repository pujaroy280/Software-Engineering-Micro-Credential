"""
Loops
Week 4 Activity 3
Puja Roy
"""
#Example 1: Use a for loop to print from 0 to 5 (exclusive)
print('\n------EXAMPLE 1-------\n')
for x in range(0,5):
    print('Counter is: ', x)

# Example 2: Use for loop to print each item in a list
print('\n------EXAMPLE 2-------\n')
fruits = ['apple','pears','grapes','orange','kiwi']
for p in fruits:
    print(p)
    
# Example 3: Use for loop to print from the 2nd item to the end
print('\n------EXAMPLE 3-------\n')
for n in range(1,len(fruits)):
    print('Fruit, ', n+1, fruits[n] )

# Example 4: For loop to print numbers between 2 and 30 (inclusive) with an increment of 3
print('\n------EXAMPLE 4-------\n')
for m in range(2,31,3):
    print(m)

# Example 5: For loop to print numbers from 10 to 0 with a decrement of 2
print('\n------EXAMPLE 5-------\n')
for z in range(30,-20,-2):
    print(z)

# Example 6: For loop to print each character of a string
print('\n------EXAMPLE 6-------\n')
wordString = 'Puja Roy'
for r in wordString:
    print(r)

# Example 7: For loop and if statement: use a for loop to print numbers from 0 to 10 exclusive, and stop/break the for loop with the counter reaches to 5
print('\n------EXAMPLE 7-------\n')
for t in range(0,10):
    print(t)
    if t == 5:
        break

# Example 8: For loop and if statement: use a for loop to print numbers from 0 to 10 exclusive, and stop/break the for loop with the counter reaches to 5
print('\n------EXAMPLE 8-------\n')
for t in range(0,10):
    if t == 5:
        break
    print(t)

# Example 9: Use for loop to print all odd numbers from 0 to 10
print('\n------EXAMPLE 9-------\n')

for q in range(0,10):
    if q%2==0:
        continue
    print(q)

# Example 10: Use a for loop to print from 3 to 0 (inclusive) and print a message GO!
print('\n------EXAMPLE 10-------\n')
for n in range(3,-1,-1):
    print(n)
else:
    print('GO!')

# ACTIVITY 3A 
print('\n------ACTIVITY 3A-------\n')
#empty list is created
fruit_list =[]
#getting the no. of fruits
nofruits = int(input("Enter the number of Fruits: "))
#for loop is used to get the fruits name one by one
for i in range(nofruits):
    print("Fruit",i+1,": ")
    #read the name of the fruit name
    fruit_item  = input()
    #add the fruit name to the fruit list using append() method
    fruit_list.append(fruit_item)
#display the fruit list using format method in string
print("User created a list of {0} items and entered the values : {1}".format(nofruits,fruit_list))

# ACTIVITY 3B 
print('\n------EXERCISE 3: Print Between a Specific Range-------\n')
number1 = int(input('Enter Number 1: '))
number2 = int(input('Enter Number 2: '))
bool = True
while (bool):
    if(number1<number2):
        print(number1)
        number1 = number1+1
        if number1==number2:
            bool = False
    else:
        print(number2)
        number2 = number2+1
        if number2==number1:
            bool = False
