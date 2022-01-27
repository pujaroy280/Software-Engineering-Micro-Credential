"""
Week 4 - Activity 2
Puja Roy
Jan 26, 2022

# Example 1: List with positive index
fruit = ['apples','orange','grapes','cherry','kiwi','melon','mango']
print(fruit[3])  # If you want to print the 4th item in the list, you have to write index 3 in brackets to get that output.

# Example 2: Use a negative index to access the 3rd item in the fruit list
print(fruit[-5])

# Example 3: Slide ==> range of indexes. Access from item 2 to item 5.
print(fruit[1:5])   #Slicing
print(fruit[5:1])   # Returns empty because it can not read it through that way.

# Example 4: Slide ==> Negative indexes. Access from item 3 to 6.
print(fruit[-5:-1])

# Example 5: Operator to concatenate lists
names = ['John', 'Martha', 'Cesar', 'Peter']
cars = ['Nisaan', 'Mazda', 'Dodge', 'Ford', 'Kia', 'Jeep']
users = cars + names
print(users)

# Example 6: + operator to concatenate items in a list
user1 = names[2] + " " + cars[4]
print("Example 6: ", user1)

# Example 7: * operator to triple the items in names
names1 = names*3
print("Example 7: ", names1)

# Example 8: Delete the 6th item in names1 list
del names1[5] #Command
print('Example 8: ', names1)
copyName = names
# Example 9: Add the name to Charles to the end of list names
names.append('Charles')
print('Example 9: ', names)
print('copyName: ', copyName)

# Example 10: extend() method to add elements from one list to another
# Add list cars into names
cars.extend(names)
print('Example 10: ', cars)

# Example 11: Clear list names
names.clear()
print('Example 11: ', names)

# Example 12: pop() removes an element from the list with specific index.
# Remove the 2nd item from the list cars
carPop = cars.pop(1)
print('Example 12: ',cars, carPop)

# Example 13: Reverse the order of the elements
cars.reverse()

# Example 14: Sort list users
users.sort()
print('Example 14: ', users)

# Example 15: copy() method returns a copy of the list
copyUsers = users.copy()
print('Example 15: ', copyUsers)
users.append('NICKY')
print('users lists ', users)
print('copyUsers ', copyUsers)

# Conditional Statement
# If Statement
age = 15
if age>=21:
    print("You are an adult!")
print("This paragraph is outside the if statement!")

# Example 16: If else Statement
if age>=21:
    print("You are an adult!")
else:
    print("You are under 21!")
print("This paragraph is outside the if else statement!")
          
"""

# ACTIVITY 2A
print('-----------ACTIVITY 2 A --------------------------------')
cities=["Bronx","Brooklyn","Manhattan","Queens","Staten Island"]
animals=["cat","dog","elephant"]
print(animals[2])
print(cities[-4:-1])
newList1=cities+animals
s=input("Select any from new List : ").strip()
newList1.remove(s)
newList1.sort()
print(newList1)
newList2=newList1+newList1
print(newList2)
print(newList2[::-1])

# ACTIVITY 2B
print('-----------ACTIVITY 2 B: FINAL GRADE CALCULATOR------------')
name = input("Enter your Name: ")#Prompt user to enter name
quiz = int(input("Enter your quiz grade: "))#Prompt user to enter quiz grade
exams = int (input("Enter your exams grade: "))#Prompt user to enter exams grade
homework = int(input("Enter your homework grade: "))#Prompt user to enter homework grade
finalGrade = (quiz*0.35)+(exams*0.4)+(homework*0.25)#Final grade
if(finalGrade>=90 and finalGrade <=100):#Condition for A grade
 print("Dear: ",name)
 print("GREAT! Your final grade is ",finalGrade," and a GPA of 'A'")
elif(finalGrade>=80 and finalGrade<90): #Condition for B grade
 print("Dear: ",name)
 print("GOOD! Your final grade is ",finalGrade," and a GPA of 'B'")
elif(finalGrade>=70 and finalGrade<80): #Condition for C grade
 print("Dear: ",name)
 print("AVERAGE: Your final grade is ",finalGrade," and a GPA of 'C'")
elif(finalGrade>=60 and finalGrade<70): #Condition for D grade
 print("Dear: ",name)
 print("BORDER-LINE! Your final grade is ",finalGrade," and a GPA of 'D'")
else:  #Condition for E grade
 print("Dear: ",name)
 print("FAIL! Your final grade is ",finalGrade," and a GPA of 'F'")
