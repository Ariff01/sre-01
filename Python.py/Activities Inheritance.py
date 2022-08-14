Activity 0
Before beginning, create a class Noun to use as the starting point for the activities in this section.
The Noun class can be anything you wish, as long as it meets the following criteria:

Do not use people or animals.
The category must be broad enough to include different examples of the category.
It must represent a real-life object.
Include at least three attributes that are common to most (if not all) instances of the Noun. 
Use appropriate naming conventions. If you created a Noun class for an earlier activity in this course,
you are welcome to use it for the activities in this page, or you can create a new one.

Implement the appropriate __init__ and display methods to create and display objects respectively.

Activity 1
Use inheritance to create another class that will inherit from the Noun class. 
Create two objects using the new class and display each object's information using the display method.

As an example from this lesson, we started with an Animal class, created a Mammal class that inherits from Animal, 
and then created two Mammal objects. You will need to identify an appropriate class based on your own Noun class as well as
appropriate objects that represent the inherited class.

class car:
    wheels=4        
    def __init__(self, brand, model, price,fuel='Gas'):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel  = fuel
    def exterior(self,colour,door):
        return f"The {self.model} {self.brand} car is {colour} coloured and has {door} doors"  
class motorbike(car):
        pass
bike1=motorbike("Honda","CBR250",9000)        

Activity 2
Add at least two attributes to the new class created in the previous activity. 
These attributes should be different from the attributes in the original Noun class and specific to the new class.

As an example from the lesson, the Animal class included the attributes of name and place.
The Mammal class that inherits from the Animal class would include mammal-specific attributes, such as gender and fur length.

Override the __init__ and display methods to display the new attributes, 
and then create at least two new objects based on the inherited class and display them with the class attributes.

class car:
    wheels=4        
    def __init__(self, brand, model, price,fuel='Gas'):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel  = fuel
    def exterior(self,colour,door):
        return f"The {self.model} {self.brand} car is {colour} coloured and has {door} doors"  
    def display(self):
        print(f"The vehicle {self.model} {self.brand} has {self.wheels} wheels and runs on {self.fuel} fuel.\nEstimated market price is ${self.price}")
class motorbike(car):
    def __init__(self, brand, model, price,fuel):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel  = fuel
bike1=motorbike("Honda","CBR250",9000,"Diesel")  
bike2=motorbike("Yamaha","R15",6000,"Diesel")
print(f"{bike1.display()\n{bike2.display()})"

Activity 3
Create a second and a third class that inherit from the Noun class you started with.

Include at least three class-specific attributes for each class.
For each of the new classes, override the __init__ and display methods to display the new attributes.
Create at least two new objects based on the inherited class and display them with the class attributes.

class truck(car):
    def __init__(self, brand, model, price,fuel,seats,tailgate):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel  = fuel
        self.seats = seats
        self.tailgate = tailgate
    
    def display(self):
      print(f"The vehicle {self.model} {self.brand} has {self.seats} seats and runs on {self.fuel} fuel with a tailgate that is {self.tailgate}.\nEstimated market price is ${self.price}")

truck1=truck("Toyota","Tundra",57500,'diesel',2,'adjustable')

truck1.display()    
    

class van(car):
    def __init__(self, brand, model, price,fuel,door,colour):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel  = fuel
        self.door  = door
        self.colour = colour
    def display(self):
        print(f"The vehicle {self.model} {self.brand} has {self.door} doors,{self.colour} coloured and runs on {self.fuel} fuel.\nEstimated market price is ${self.price}")

van1=van("Toyota","Sienna",42500,"diesel","automatic","white")
van1.display() 
    


Activity 4
Using the three inherited classes you have already created, 
use the __init__ method of the Noun class to set the values of the original attributes defined in the Noun class.

Create two objects for each of the three inherited classes and display all attributes, including attributes from the original Noun class.
class motorbike(car): 
   def __init__(self, brand, model, price,fuel='Diesel'):
        car.__init__(self, brand, model, price,fuel='Gas')
        self.fuel  = fuel
bike2=motorbike("Honda","CBR250",9000,"Diesel")        
        
class truck(car):
    def __init__(self, brand, model, price,fuel,seats,tailgate):
        car.__init__(self, brand, model, price,fuel='Gas')
        self.seats = seats
        self.tailgate = tailgate
        self.fuel=fuel
    def display(self):
      print(f"The vehicle {self.model} {self.brand} has {self.seats} seats and runs on {self.fuel} fuel with a tailgate that is {self.tailgate}.\nEstimated market price is ${self.price}")
        
truck2=truck("Toyota","Tundra",57500,'diesel',2,'adjustable')


class van(car):
    def __init__(self, brand, model, price,fuel,door,colour):
        car.__init__(self, brand, model, price) 
        self.door  = door
        self.colour = colour 
        self.fuel=fuel
    def display(self):
        print(f"The vehicle {self.model} {self.brand} has {self.door} doors,{self.colour} coloured and runs on {self.fuel} fuel.\nEstimated market price is ${self.price}")
        
van2=van("Toyota","Sienna",42500,"diesel","automatic","white")

print(bike2.display())
print(truck2.display())
print(van2.display())

Activity 5
Create a class that inherits from your initial inherited class. Include at least one attribute specific to this class.
Create two objects based on this class and display all attributes for each object.

class toytruck(truck):
    def __init__(self, brand, model, price,fuel,seats,tailgate,toyshop):
        truck.__init__(self, brand, model, price,fuel,seats,tailgate)
        self.toyshop=toyshop
    def display(self):
        print(f"The toy vehicle {self.model} {self.brand} has {self.seats} seats and runs on {self.fuel} fuel with a tailgate that is {self.tailgate}.\nPrice is ${self.price} and sold in {self.toyshop}")
toytruck1=toytruck("toyota","cbr7",35,'battery',2,'removable',"ToysRUs")
toytruck2=toytruck("Nissan","GZ11",7.99,'battery',4,'fixed','Simply Toys')

print(toytruck1.display())
print(toytruck2.display())

Activity 6
Create another class that inherits from the class created for the previous activity.
For the new class, create at least one class-specific attribute and one object based on the class.

Use isinstance() to verify that the new object is an instance of each of the parent classes of the new class.

class toymanufactorer(toytruck):
    def __init__(self, brand, model, price,fuel,seats,tailgate,toyshop,manufactorer):
        toytruck.__init__(self, brand, model, price,fuel,seats,tailgate,toyshop)
        self.manufactorer=manufactorer
    def display(self):
        print(f"The toy vehicle {self.model} {self.brand} was manufactored by {self.manufactorer}\nhas {self.seats} seats and runs on {self.fuel} fuel with a tailgate that is {self.tailgate}.\nPrice is ${self.price} and sold in {self.toyshop}")
        
toymanu1=toymanufactorer("toyota","cbr7",35,'battery',2,'removable',"ToysRUs","Global United Toys")

print(isinstance(toymanu1,toytruck))
print(isinstance(toymanu1,truck))
print(isinstance(toymanu1,car))

<output>
True
True
True






