Write a program that will calculate the cost of a custom cup of coffee at a gourmet coffee shop, based on the size of the cup, the type of coffee selected,
and flavors that can be added to the coffee. It should complete the following steps:

Ask the user what size cup they want, choosing between small, medium, and large.
Ask the user what kind of coffee they want, choosing between brewed, espresso, and cold brew.
Ask the user what flavoring they want, if any. Choices include hazelnut, vanilla, and caramel.
Calculate the price of the cup using the following values:
Size:
small: $2
medium: $3
large: $4
Type:
brewed: no additional cost
espresso: 50 cents
cold brew: $1
Flavoring:
None: no additional cost
All other options: 50 cents
Display a statement that summarizes what the user ordered.
Display the total cost of the cup of coffee as well as the cost with a 15% tip, in phrases that explain the values to the user.
Round the cost with tip to two decimal places.
For example, if the user asks for a medium-sized espresso with hazelnut flavoring, the total should be $4; the total with a tip should be $4.60.

#code
c=0
tc=0
size=input("what size cup do you want? (small,medium,large)").lower()
type=input("What type of coffe do you want? (brewed,espresso,cold brew)").lower()
flavor=input("Do you want flavored syrup, if so what type? (no, hazelnut, vanilla, or caramel)").lower()
if size=="small":
  c+=2
elif size=="medium":
  c+=3
elif size=="large":
  c+=4
if type=="espresso":
  c+=0.5
elif type=="cold brew":
  c+=1
if flavor=="hazelnut" or flavor=="vanilla" or flavor=="caramel":
  c+=0.5
tc=round(c*1.15,2)
print(f"You asked for {size} cup of {type} coffee with {flavor} syrup\nYour cup of coffee costs ${c} and with tip costs ${tc}")

