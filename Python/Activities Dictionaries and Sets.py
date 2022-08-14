Activity 1
Create a program that sums all the values in a dictionary and displays them.

For example:

dictionary = {"hello":4,"world":4,"I":1,"am":2,"Martha":3}
output: 14 (the result of 4 + 4 + 1 + 2 + 3)
#code



Activity 2
Write a program that displays the maximum and minimum values in a dictionary.
You may use the same dictionary you used in the previous activity or create a new one.

max(dictionary.values())
min(dictionary.values())

Activity 3
Write a program that returns the sum of the integer elements in a set.
sum(set)

Activity 4
Write a program that computes and displays the maximum and the minimum values in a set.
max(set)
min(set)

Activity 5
Given the following dictionary storage, complete the following tasks:

Add a key named "freezer".
Set the value of "freezer" to be a list containing the items "ice cubes", "ice cream", and "pepperoni pizza".
Sort the items in the cupboard using sort.
Add "cream" to the fridge.
Remove "sugar" from the cupboard.
Subtract $25 from the emergency jar.
storage = {
    "cupboard" : ["spices", "flour", "sugar"],
    "drawer" : ["fork", "knife", "spoon"],
    "fridge" : ["butter", "milk", "cheese"],
    "emergency jar" : 150
}
 
# your code here
storage['freezer']=["ice cubes", "ice cream", "pepperoni pizza"]
storage['cupboard'].sort()
storage['fridge'].append('cream')
storage['cupboard'].remove('sugar')
storage['emergency jar']-=25



Activity 6
Create a new dictionary named shopping_list and add the following items to the dictionary:

"milk" : 4,
"butter" : 2,
"crackers" : 1.5,
"rice" : 2.25,
"spaghetti" : 1.75,
"dish soap": 3.25
Loop through each item in the list and print out each key with its price. Print the answer in this format:

milk
price: 4
Next, calculate how much it will cost if you purchase all the items on the list.

Use a variable named total_cost to store the calculated value.
Loop through the dictionary and add the price of each item to the total cost.
After looping through the dictionary, print out the total cost in a message that is meaningful to the user.

#code
shopping_list={"milk" : 4,
"butter" : 2,
"crackers" : 1.5,
"rice" : 2.25,
"spaghetti" : 1.75,
"dish soap": 3.25}

for i,j in shopping_list.items():
    print(i,f"price: {j}",sep='\n')
    

#total cost with loop
total_cost=0
for v in shopping_list.values():
  total_cost+=v
print(f"The total price of your shopping list is: {total_cost}")  

or  
#total cost
print(f"The total price of your shopping list is: {sum(shopping_list.values())}") 



Activity 7
Create two dictionaries: price and quantity.

The price dictionary should be the same as the shopping_list dictionary in the previous activity:
"milk" : 4,
"butter" : 2,
"crackers" : 1.5,
"rice" : 2.25,
"spaghetti" : 1.75,
"dish soap": 3.25
The quantity dictionary should have the same keys, but with values that represent the number of items to purchase rather than the price:
"milk" : 1,
"butter" : 1,
"crackers" : 3,
"rice" : 2,
"spaghetti" : 5,
"dish soap": 1
Write a script that loops through both dictionaries to calculate the total cost if we purchase the indicated quantity of each item in the dictionaries.

#code
total_sum=0
for v1,v2 in zip(price.values(),quantity.values()):
    total_sum+=v1*v2
print(f"The total price of the shopping list given the quantity and price is: ${total_sum}") 

