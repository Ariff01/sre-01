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
Repeat until the user enters "quit."
When the user enters "quit," display the original set, the final version of the updated set, and the difference between the two sets.

#Ariff
#10 August 2022
#code

nset={'sweet','orange','sour','apple','bitter'}
numset=nset.copy()
q=''
while q!='quit':
  val=input('Please input a value: ').lower()
  op=input('Please input an operation: (add,remove) ').lower()
  if op=='add':
    if val in numset:
      print("The value exists in the set")
    else:
      numset.add(val)
      print(numset)
  elif op=='remove':
     if val not in numset:
       print("The value edoes not exist")
     else:
       numset.remove(val)
       print(numset)
  else:
     print("please input the correct operation: (add,remove)")
  q=input("Input 'quit' to exit program and view results, else click <enter> to continue with the edit: ").lower() 
print(f'oldset = {nset}\nnewset = {numset}\nDifference between oldset and newset: {nset-numset}\nDifference between newset and oldset: {numset-nset}')

