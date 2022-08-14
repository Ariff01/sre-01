The activities in this page will allow you to demonstrate your ability to:

Create a class that includes at least three attributes appropriate for that class.
Use a class to create two or more separate objects.
Define and use a constructor in a class.
Create one or more methods that describe a behavior associated with a class and implement those methods in a program.
Reference a class as an attribute of another class to create a complex entity.

Activity 1
The lesson uses Person and Animal as example classes. For this activity, choose another Noun of your choice to create a class.
It can be anything you wish, as long as it meets the following criteria:

Do not use people or animals.
The category must be broad enough to include different examples of the category.
It must represent a real-life object.
Include at least three attributes that are common to most (if not all) instances of the Noun. Use appropriate naming conventions.


class car:
    wheels=4
    fuel='Gas'
    
   
    
Activity 2
Use the Noun class you created in the previous activity to create at least four different objects. Print out all attributes for each object.
car1=car()
car2=car()
car3=car()
car4=car()

print(car1.wheels,car1.fuel)


Activity 3
Create an __init__ method for your Noun class. Include at least four of the attributes you originally defined in the new method.

class car:
    wheels=4
    
    

    def __init__(self, brand, model, price,fuel='Gas'):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel  = fuel

Activity 4
Create a method for your Noun class. The method should perform a specific activity (or series of activities) on objects based on the class.

class car:
    wheels=4
    
    

    def __init__(self, brand, model, price,fuel='Gas'):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel  = fuel
        
    def exterior(self,colour,door):
        return f"The {self.model} {self.brand} car is {colour} coloured and has {door} doors"
        



Activity 5
Create a separate class that is logically related to your original Noun class, based on the example that a Person can have one or more Addresses.

Create at least one Noun object that includes a list of objects from the associated class. Display the Noun with the related objects.

class cardealership():

    def __init__(self, name, country, cars):
            self.name = name
            self.country = country
            self.cars=cars
    def display(self):
            print(f"The name of this dealership is {self.name},based in {self.country} and contains these cars: ")
            for i in self.cars:
                print(vars(i))
                
car1=car('Audi','R8',800000)
car2=car('BMW','I8',700000)
carset=[car1,car2]

dealer1=cardealership('Vincar','Singapore',carset)
dealer1.display()
    
    
