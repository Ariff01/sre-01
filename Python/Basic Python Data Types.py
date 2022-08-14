Activity 1
Create a computer program that performs the following steps:

Prompt the user for an integer and store the value in a variable.
Display the data type of the variable that holds the entered data.
Convert the value to an integer type and store the converted value in a new variable.
Display the value and type of the new variable in a single sentence. (For example, "The value is 8 with type integer.")
Run the program and enter a float value at the prompt.
What is its value in the last step?

Refactor the program, using a float instead of an integer. What happens if you enter an integer rather than a float at the prompt?

val=input("Please key in an integer: ")
print(type(val).__name__)
valint=int(val)
print(f"The value is {valint} with datatype: {type(valint).__name__}")

#Run program with float input,4.6,output is error 
#Refactor the program, using a float instead of an integer.After entering integer,5, output is: 
#str
#The value is 5.0 with datatype: float

#Hence, str that is in an integer format can be converted to a float but str in float format cannot be converted to str 

Activity 2
Update the code below so that the result is equal to 576. Do not change any of the existing values or operators or the order in which they appear.

# do not change the order in which the numbers and operators appear in the next line
result = 5 + 3 ** 2 * 9 + 490
 
print(result) # the output should be 576

Activity 3
Create a computer program that prompts the user for a float number and returns the integer portion of the floating number.
import math
x=float(input("Input float number: "))
print(math.floor(x))

Activity 4
Write a computer program that calculates and displays the current value of a deposit for a given initial deposit, interest rate, 
how many times interest is calculated per year, and the number of years since the initial deposit.

The program should prompt the user for each of the values and use the following formula to calculate the current value of the deposit:

V = P(1 + r/n)^nt
where

V -- value
P -- initial deposit
r -- interest rate as a fraction (eg 0.05)
n -- the number of times per year interest is calculated
t -- the number of years since the initial deposit
The program should display each of the values entered to the user in a meaningful way 
(so that the user can easily see what each value represents), along with the results of the calculation.


#ANS
p=float(input("Input your initial deposit: "))
r=float(input("Input the interest rate in decimal: "))
n=int(input("Input the number of times interest is calculated per year: "))
t=int(input("Input the number of years its been since the initial deposit year: "))
v=round(p*(1 + (r/n))**(n*t),2)
print(f"Your initial deposit is ${p}. \nInterest is calculated {n} times per year, \nwhereby interest rate is {r} \
\nand it has been {t} years since your intial deposit \nYour current deposit value after interest is ${v}")

Activity 5

Write a computer program that prompts the user for a principal amount, the rate of interest, 
and the number of days for a loan and then calculates and returns the simple interest for the life of the loan. Use the formula:
interest = principal * rate * days / 365

#ANS
p=float(input("Please input the pricipal loan amount: "))
r=float(input("Please input the interest rate in decimal: "))
n=int(input("Please input the number of days since the loan: "))
i=round(p*r*(n/365),2)
print(f"Simple interest for the loan is ${i}")


Activity 6
Create a computer program that displays three statements that evaluate to True and three statements that evaluate to False.

a="1";b=1;c=2;
d="apple";e="3";f=3

print("a is not b:",a!=b,"\nc is greater than b:",c>b,"\nDifference between c and b is 1:",
      c-b==1,"\ne equals to f:",e==f,"\nDifference between f and c is a:",
      f-c==a,"\nIndex 1 of string d is 'a':",d[1]=="a")
      
Activity 7
Create a computer program that prompts the user for a number and calculates the following:

the boolean of the number entered
the binary equivalent of the number entered
the square root of the number entered

The program should display the following to the user:

The number the user entered, in a phrase like, "You selected value."
The boolean of the number, in a phrase like, "The boolean of your number is value."
The binary equivalent of the number, in a phrase like, "The binary equivalent of your number is value"
The square root of the number, in a phrase like, "The square root of your number is value," with the value rounded to three decimal places.

x=int(input("Input float number: "))
print(f"You selected {x}\nThe boolean of your number is",bool(x),
      "\nThe binary equivalent of your number is:",bin(x),"\nThe square root of your number is:",round(x**0.5,3))

Activity 8
Create a computer program that completes the following tasks:

It prompts the user for a series of 5 integers.
The user must be prompted for 5 numbers.
After the fifth entry, the program stops prompting for values and performs the following calculations:
the product of the integers
the average of the integers
the sum of the integers
After performing the calculations, the program should display the following to the user:
the values the user entered
each of the calculations, using a phrase that identifies the value      

import math
num=[int(input("Input an integer ")) for i in range(5)]
product=math.prod(num)
total=sum(num)
avg=sum(num)/len(num)
print(f"Values entered were: {num}\nProduct of the numbers: {product}\nAverage of the numbers: {avg}\nSum of the numbers: {total}")

Activity 9

Write a program that performs the following steps:

Start with a street address that includes a building/house number, the name of the street, and the type of street (e.g., Street, Avenue, Boulevard, etc.).
You can use any address you wish and abbreviations are acceptable.
An example is 25 Main Street.
Display the full address to the user.
Display the house number only in a phrase like, "The building or house number is 25."
Display the street name in a phrase like, "The street name is Main Street."

house="117 Queen's Street"
print(f"The full address is {house}\nThe house number is {house.split()[0]}\nThe street name is{house.split('7')[1]}")

or

print(f"The full address is {house}\nThe house number is {house.split()[0]} \
\nThe street name is {house.split()[1]+' '+house.split()[2]}")

