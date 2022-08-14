Activity 1
Write a program that asks the user how much money they have in their wallet. 
The program should output "You're rich!" if the user inputs $20 or more and "You're broke!" if the input is less than $20.

mon=float(input("Input how much money you have in your wallet: "))
if mon>=20:
  print("You're rich!")
else:
  print("You're broke!")
  
Activity 2
Write a program that performs the following steps:

Ask the user if they own any cats. (Yes/No answer)
Ask the user if they own any dogs. (Yes/No answer)
If the user responses indicate that they have both cats and dogs, output "You must really love pets!"
Otherwise, the output should be "Maybe you need more pets."
The last step will apply if the user has cats but not dogs, dogs but not cats, or neither cats nor dogs.

Write two different versions of this program, one that uses only if statements and another that uses if-else statements.  

#version 1
cat=input("Do you own any cats?(yes/no)")
dog=input("Do you own any dogs?(yes/no)")

if cat=="yes" && dog=="yes":
  print("You must really love pets!")
if cat=="no" or dog=="no"
  print("Maybe you need more pets.")
  
#version 2
cat=input("Do you own any cats?(yes/no)")
dog=input("Do you own any dogs?(yes/no)")

if cat=="yes" && dog=="yes":
  print("You must really love pets!")
else:
  print("Maybe you need more pets.")

Activity 3
Create a computer program that asks the user a few questions to which the user will respond either True or False. 
Display all the questions with the correct answer and the user's answers at the end of the program, 
along with the user's the correct response rate (number of questions answered correctly/number of questions).

c=0
ans1=input("Are there 5 fingers on 1 hand ").capitalize()
if ans1=='True':
  c+=1
ans2=input("Earth is flat ").capitalize()
if ans2=='False':
  c+=1  
ans3=input("Earth has an atmosphere ").capitalize()
if ans3=='True':
  c+=1
ans4=input("US president is Trump ").capitalize()
if ans4=='False':
  c+=1  
ans5=input("Plants make their own food ").capitalize()
if ans5=='True':
  c+=1    
print("The answers are ('True', 'False', 'True', 'False', 'True') and your answers are",(ans1,ans2,ans3,ans4,ans5),f"\nYou scored {c}/5")  



Activity 4
Write a program that uses elif to produce five different possible outcomes based on a single user input.

Ask the user what season it is (fall, winter, spring, or summer).
If the user enters fall, output "I bet the leaves are pretty there!"
If the user enters winter, output "I hope you're ready for snow!"
If the user enters spring, output "I can smell the flowers!"
If the user enters summer, output "Make sure your AC is working!"
If the user enters a value that does not correspond to a season, output "I don't recognize that season."
The user should be able to enter the name of the season in any case and the program will still work.

Challenge: After you have the program working as describe above, modify the program so that the user can enter either "fall" or "autumn" and get the same result.

season=input("What is the season? (fall, winter, spring, or summer)").capitalize()
if season== "Fall" or season== "Autumn":
    print("I bet the leaves are pretty there!")
elif season=='Winter':
    print("I hope you're ready for snow")
elif season=="Spring":
    print("I can smell the flowers!")
elif season=="Summer":
    print("Make sure your AC is working!")  
else:
    print("I don't recognize that season.")
