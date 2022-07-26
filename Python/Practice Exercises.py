Activity 1-10 repeated questions


Activity 11
Write a program that performs the following steps:

Start with a Contact entry that includes the following pieces of information:
A person's first and last name, e.g., Robert Taylor
A complete street address, e.g., 25 Main Street
A city, state, and zip, e.g., Paterson NJ 07501
A 10-digit phone number, e.g., 201-857-5309

Display the complete Contact data to the user.
Prompt the user to select one item in the Contact data that they want to change.
Prompt the user for the new value for that item.
Change the Contact data appropriately and display the updated Contact data to the user.

#code
firstname="Robert"
lastname="Taylor"
address="25 Main Street"
city="Paterson"
state="NJ"
zip="07501"
phone="201-857-5309"
contactstr=['firstname','lastname','address','city','state','zip','phone']
contact=[firstname,lastname,address,city,state,zip,phone]

change=input("input which data you would like to change? (firstname,lastname,address,city,state,zip,phone)")
new=input("What is the new data to input?")
for count,i in enumerate(contactstr):
  if change==i:
    contact[count]=new.strip()
print(contact)  
  


Activity 12
Write a program that allows a user to create a new Contact, including a first and last name, 
complete street address, city, state, zip, phone number, and email address.

Display the contact to the user after accepting all entries.

firstname,lastname=input("input firstname and lastname").split()
address=input("input address")
city=input("input city")
state=input("input state")
zip=input("input zip")
phone=input("input phone number")
email=input("input email address")
contact=[firstname,lastname,address,city,state,zip,phone,email]
print(contact)




Activity 13
Combine the previous two activities into a single program that performs the following steps:

Prompt the user for complete Contact details for a new contact.
Displays the Contact details entered by the user.
Prompts the user to select a value to change.
Updates the selected value with a new input value.

#code
firstname,lastname=input("input firstname and lastname").split()
address=input("input address")
city=input("input city")
state=input("input state")
zip=input("input zip")
phone=input("input phone number")
email=input("input email address")
contact=[firstname,lastname,address,city,state,zip,phone,email]
contactstr=['firstname','lastname','address','city','state','zip','phone','email']
print(contact)

change=input("input which data you would like to change? (firstname,lastname,address,city,state,zip,phone,email)")
new=input("What is the new data to input?")
for count,i in enumerate(contactstr):
  if change==i:
    contact[count]=new.strip()
print(contact)  


