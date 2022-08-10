Activity 1
Given the list fruit_list, write a script that iterates through the list and prints each item on a separate line.

fruit_list = ["apple", "banana", "cherry", "gooseberry",
"kumquat", "orange", "pineapple"]
 
# your code here
for i in fruit_list:
  print(i)



Activity 2
Write a Python script that asks the user for a string and displays the characters of the string to the user, with each character on a new line.

For example, if the input is Hello, the output should be:

H
e
l
l
o
#code
s=input("Please enter a string ")
for i in s:
  print(i)

Activity 3
Write a Python script that computes the length of a string without using the len() function.
len(string)

Activity 4
Create a program that starts with a list of strings, identifies all the strings with more than two characters,
stores the results in another list, and displays the new list.

For example:

a = ["a", "bc", "rye", "hello", "c", ""]
Output:

["rye", "hello"]

#code
b=[]
for i in a:
  if len(i)>2:
    b.append(i)
print(b)  
  


Activity 5
Write two scripts, each of which displays all numbers divisible by 50 between 100 and 1000 (inclusive).

Use the range function with for in one script.
Use while without range in the other script.
Both scripts should have identical outputs.

# script 1: range
# your code here
for i in range(100,1001):
  if i%50==0:
  print(i)


# script 2: while
# your code here
n=50
count=100
while (count<1001):
  if count%n==0:
    print(count)
  count+=1


Activity 6
Create a script that computes the sum of all numbers between 0 and 100.
sum(range(101))

Activity 7
Create a script that computes the factorial of any given number.
f=1
n=int(input("input a number"))
for i in range(1,n+1):
  f=i*f
print(f)  

Activity 8
Starting with the defined fruit_list in the code block below, update the script to perform the following tasks.

Prompt the user to enter the name of a fruit.
If the fruit is in fruit_list, display an appropriate message to the user and tell the user its index value in the list.
If the fruit is not in fruit_list, display an appropriate message to the user and prompt them to try again.
The script should repeat itself until the user enters a stop word at the prompt.
Tip: It's always a good idea to tell the user how to end a loop!

fruit_list = ["apple", "banana", "cherry", "gooseberry",
"kumquat", "orange", "pineapple"]
 
# your code here

st=""
while st!="stop":
  fr=input("Please enter name of a fruit ").lower()  
  for i,j in enumerate(fruit_list):
    if j==fr:
      print(f"the index value is: {i}")
  if fr not in fruit_list:  
    print(f"Error, your word, {fr}, was not found in the list")    
  st=input("Please input 'stop' to end the program, or click <enter> to try again ").lower() 
    
    

Activity 9
Create a script that asks the user for a variable number of values and displays the sum of those values to the user. 
The program should prompt the user for values until the user enters the word "quit" (uppercase or lowercase), 
display the values used in the calculation, and then display the total of those values.
numlist=[]
while a!="quit":
  numlist.append(int(input("Please input an integer: ")))
  a=input("Please input 'quit' to end program and view summation results, or click <enter> to continue integer input ").lower()
print(f"The numbers inputted are: {numlist}\nThe sum of these numbers are {sum(numlist)}")  



Activity 10
Write a script that asks the user for an integer value and then displays the multiplication table of that input number from 1 through the integer squared.

num=int(input("Please input an integer: "))
for i in range(1,num**2+1):
  print(f"{i} x {num} =",i*num)


Activity 11
Create a script that identifies all prime numbers between 0 and 100.

prime=[]
for i in range(2,101):
  c=0  
  for j in range(2,i):
    if i%j==0:
      c+=1  
      break
  if c==0:
    prime.append(i)
print(prime)

Activity 12
Write a script that calculates the greatest common denominator between two numbers.
def gcf(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcf(b, a % b)
    
    
num1=int(input("Please input number 1: "))
num2=int(input("Please input number 2: ")) 
print("The greatest common factor is:",gcf(num1, num2))



Activity 13
Write a Python script that computes the frequency of each digit in a given integer.

For example, if the input number is 334, the output should be:

3 occurs 2 times
4 occurs 1 time

#code
num=input("Please input an integer: ")
nums=set(num)
for i in nums:
    c=0
    for j in num:
        if i==j:
            c+=1
    print(f"{i} occurs {c} times")   


Activity 14
Write a script that calculates the lowest common multiple of two given integers.

For example, given the values 4 and 6, the lowest common multiple is 12.

def gcf(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcf(b, a % b)
def lcm(a,b):
    return (a*b)/gcf(a,b)  
num1=int(input("Please input number 1: "))
num2=int(input("Please input number 2: ")) 
print("The lowest common multiple is:",lcm(num1, num2))


Activity 15
Write a Python script that determines if an input number can be expressed as the sum of two prime numbers.

For example, the number 10 can be expressed as the sum of two prime numbers:

10 = 3 + 7 : both prime numbers
10 = 5 + 5 : both prime numbers
However, the number 11 cannot be:

11 = 1 + 10 : neither 1 nor 10 are prime numbers
11 = 2 + 9 : 9 is not a prime number
11 = 3 + 8 : 8 is not a prime number
11 = 4 + 7 : 4 is not a prime number
11 = 5 + 6 : 6 is not a prime number

#code
num=int(input("Input a number: "))
prime=[]
for i in range(2,num):
  c=0  
  for j in range(2,i):
    if i%j==0:
      c+=1  
      break
  if c==0:
    prime.append(i)
c=0
for i in range(2,num//2+1):
    if i in prime and (num-i) in prime:
        c+=1
        break        
if c==1:
    print(f"Yes, {num} can be expressed as a sum of 2 prime numbers:",i,f"and {num-i}")
else:
    print(f"No,there isn't 2 prime numbers to add up to {num}")

