Your company has organized a morale event! They're hosting a picnic and field day in the park, and of course, they want to play games! Team games! Team building games!

To do that they want to assign the attendees to certain teams based on their last name. They've already chosen the team names, but they want you to write a program that will sort each person into the correct team.

Here are the specs:

If a person's name starts with A, B, C, or D, then they are on the team "Red Dragons"
If the name starts with E, F, G, or H, they are on the team "Dark Wizards."
If the name starts with I, J, K, or L, they are on the team "Moving Castles."
If the name starts with M, N, O, or P, they are on the team "Golden Snitches"
If the name starts with Q, R, S, or T, they are on the team "Night Guards."
If the name stars with U, V, W, X, Y, or Z, they are on the team "Black Holes."

name=input("Please input your last name: ").lower()
if name[0] in ['a','b','c','d']:
  print("Youre are in 'Red Dragons' team!")
elif name[0] in ['e','f','g','h']:
  print("Youre are in 'Dark Wizard' team!")
elif name[0] in ['i','j','k','l']:
  print("Youre are in 'Moving Castles' team!")  
elif name[0] in ['m','n','o','p']:
  print("Youre are in 'Golden Snitches' team!")   
elif name[0] in ['q','r','s','t']:
  print("Youre are in Night Guards' team!")  
elif name[0] in ['u','v','w','x','y','z']:
  print("Youre are in 'Black Holes' team!")  
else:
  print("Unfamiliar input,try again")
print("good luck in the games!")  
