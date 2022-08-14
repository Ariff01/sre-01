Activity 1
Prompt the user to answer a series of 3-5 questions about themselves (such as their name, their age, their birthday, or where they live) and save the answers in a list. Display the results to the user.

name=input("What is your name?")
age=int(input("What is your age?"))
add=input("Where do you stay?")
q=[name,age,add]
# your code here
name=input("What is your name?")
age=int(input("What is your age?"))
add=input("Where do you stay?")
q=[name,age,add]
print(q)
Activity 2
Present the user with an existing list of items (such as the list created in the previous activity) and prompt the user for 2-4 more items to add to the list. Update the list with the new items and display the updated list.

# your code here
name=input("What is your name?")
age=int(input("What is your age?"))
add=input("Where do you stay?")
q=[name,age,add]
print(q)
​
c=0
while c<4:
    add=input("please add another item to the list:")
    q.append(add)
    quit=input("Do you want to quit?(yes/no) *only if updated minimum of 2*: ").lower()
    c+=1
    if c>1 and quit=='yes':
        break
q     

What is your name?Ariff
What is your age?1
Where do you stay?sg
['Ariff', 1, 'sg']
please add another item to the list:male
Do you want to quit?(yes/no) *only if updated minimum of 2*: no
please add another item to the list:singapore
Do you want to quit?(yes/no) *only if updated minimum of 2*: yes
['Ariff', 1, 'sg', 'male', 'singapore']

Activity 3
Present the user with a list of 7-9 items (such as the list created in the previous activities) and prompt them to enter one item to delete from the list. Delete the named item from the list and display the updated list.

5
# your code here
list1=['Ariff', '5', 'sg', 'male', 'singapore','1','2','3']
print(list1,"\nWhat would you like to remove from this list? ")
rem=input()
list1.remove(rem)
print(f"Updated list\n{list1}")
​
['Ariff', '5', 'sg', 'male', 'singapore', '1', '2', '3'] 
What would you like to remove from this list? 
singapore
Updated list
['Ariff', '5', 'sg', 'male', '1', '2', '3']

Activity 4
Present the user with a list of 7-9 items (such as the list created in the previous activities) and prompt them to select one item from the list to update, along with the new value for that item. Change the item's value and display the new list to the user.

# your code here
list2=['Ariff', '5', 'sg', 'male', 'singapore', '1', '2', '3'] 
print(list2)
print('What would you like to update?')
old=input()
num=list2.index(old)
new=input("What would you like to change it with? ")
list2[num]=new
print(f'Updated list: {list2}')
['Ariff', '5', 'sg', 'male', 'singapore', '1', '2', '3']
What would you like to update?
sg
What would you like to change it with? ny
Updated list: ['Ariff', '5', 'ny', 'male', 'singapore', '1', '2', '3']

Activity 5
Create four tuples:

One tuple with a person's first name and last name
A second tuple with the person's current profession
A third tuple with the person's current address
A fourth tuple with the person's previous address
Combine all tuples into a new, single tuple that contains all items from the original tuples.

# your code here
name=('George','Bush')
pro=('SRE','Engineer')
cadd=('Golden','State')
oadd=('River','Dale')
print(name+pro+cadd+oadd)
('George', 'Bush', 'SRE', 'Engineer', 'Golden', 'State', 'River', 'Dale')

Activity 6
Create a program that completes the following tasks:

Prompt the user for a series of 5-10 integers.
The user must be prompted for a minimum of five numbers.
After the user has entered five numbers, allow the user to stop or enter another number.
When the user chooses to stop or after ten numbers have been entered, stop prompting for values and perform calculations to find the following:
The product of the integers
The average of the integers
The sum of the integers
The min of the integers
The max of the integers
After performing the calculations, display the following to the user:
The values the user entered
Each of the calculations, using a phrase that identifies the value
Do not use the built-in sum, min, or max functions.

 
# your code here
num=[]
for i in range(1,11):
    
    num.append(int(input('Please input an integer: ')))
    if i>=5:
        quit=input("Do you want to quit?(yes,no): ").lower()
        if quit=='yes':
            break
mi=num[0];ma=num[0];s=0;p=1;
for j in num:
    s+=j
    p*=j
    if j<mi:
        mi=j
    if j>ma:
        ma=j
    avg=s/len(num)    
print(f"Values entered:{num}\nThe product of numbers: {p}\nThe average of numbers: {avg}\nThe sum of numbers: {s}\n \
The minimum of numbers: {mi}\nThe maximum of numbers: {ma}")
​
        
​
Please input an integer: 1
Please input an integer: 2
Please input an integer: 3
Please input an integer: 4
Please input an integer: 5
Do you want to quit?(yes,no): yes
Values entered:[1, 2, 3, 4, 5]
The product of numbers: 120
The average of numbers: 3.0
The sum of numbers: 15
 The minimum of numbers: 1
The maximum of numbers: 5

Activity 7
Create a program that takes an input list of strings, identifies all the strings with more than two characters, and stores the results in another list.

For example:

a = ["a", "bc", "rye", "hello", "c", ""]
Output:

["bc", "rye", "hello"]
=
# your code here
a = ["a", "bc", "rye", "hello", "c", ""]
b=[]
for i in a:
    if len(i)>=2:
        b.append(i)
print(b)        
['bc', 'rye', 'hello']

Activity 8
Write a program using the steps below:

Create a dictionary with at least three key-value pairs.
Ask the user for a value.
Display all key-value pairs in the dictionary that include the user-specified value.
If the value does not exist in the dictionary, display a user-friendly error message.
For example:

dictionary: freq_count = {"hello":4,"world":4,"I":1,"am": 2,"Martha:"3"}
user input: 4
output: {"hello":4,"world":4}
# your code here
freq_count = {"hello":4,"world":4,"I":1,"am": 2,"Martha": 3}
user=int(input("Please input an integer: "))
c=0
for i,j in freq_count.items():
              if j==user:
                print(f"{i}:{j}")
                c+=1
if c==0:
    print("Value is not found")
Please input an integer: 7
Value is not found

Activity 9
Create a program that does the following:

Define a set with at least five elements.
Ask the user for a value.
Ask the user for an operation ("add" or "remove").
If the operation is "remove":
If the value exists in the set, remove the value from the set and display the updated set to the user.
If the value does not exist in the set, display a user-friendly error message.
If the operation is "add":
If the value exists in the set, display a user-friendly error message.
If the value does not exist in the set, add the value to the set and display the updated set to the user.
Repeat until the user enters "quit" (uppercase or lowercase).
repeated
# your code here
repeated
