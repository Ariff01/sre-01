
Object-oriented programming is a programming paradigm that provides a means of structuring programs as class
so that properties and behaviors are bundled into individual objects through creating instances of the class

class: is a blueprint for how something should be defined. It doesn’t contain actual data, just the properties. 

object: There are various types of objects in Python such as Lists, dictionaries, files, integers, sets, strings etc. 
An object is defined by its class. For example, an integer variable is a member of the integer class. An object is a physical entity. 
State, Identity, and behavior are the three key properties of the object.
an object could represent a person with properties like a name, age, and address and behaviors such as walking, talkin

instance: While the class is the blueprint, an instance is an object that is built from a class and contains real data. 

attribute: A value associated with an object which is referenced by name using dotted expressions.
For example, if an object o has an attribute a it would be referenced as o.a

method: A function which is defined inside a class body. If called as an attribute of an instance of that class, 
the method will get the instance object as its first argument (which is usually called self). See function and nested scope.

__init__() method initializes each new instance of the class,
sets the initial state of the object by assigning the values of the object’s properties.

the first parameter will always be a variable called self. When a new class instance is created, 
the instance is automatically passed to the self parameter in .__init__() so that new attributes can be defined on the object.

instance attributes: Attributes created in .__init__() are called instance attributes. An instance attribute’s value is specific to a particular instance of the class. 
All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.

class attributes: attributes that have the same value for all class instances. 
You can define a class attribute by assigning a value to a variable name outside of .__init__().

class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

class dog with init method and attributes of name and age     
the statement "self.name = name", creates an attribute called name and assigns to it the value of the name parameter.

>>> a = Dog()
>>> b = Dog()
>>> a == b
False
This is because the a and b are both instances of the Dog class, but they represent two distinct objects in memory.

>>> buddy = Dog("Buddy", 9)
>>> miles = Dog("Miles", 4)

After you create the Dog instances, you can access their instance attributes using dot notation:

>>> buddy.name
'Buddy'
>>> buddy.age
9
>>> buddy.species
'Canis familiaris

Although the attributes are guaranteed to exist, their values can be changed dynamically:

>>> buddy.age = 10
>>> buddy.age
10

Instance methods are functions that are defined inside a class and can only be called from an instance of that class
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
        
>>> miles = Dog("Miles", 4)

>>> miles.description()
'Miles is 4 years old'

>>> miles.speak("Woof Woof")
'Miles says Woof Woof'


 Inheritance is the process by which one class takes on the attributes and methods of another. 
 Newly formed classes are called child classes, and the classes that child classes are derived from are called parent classes.
 Child classes can override or extend the attributes and methods of parent classes.
 
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
        
create child class with its own name and then put the name of the parent class in parentheses. 
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

create instances of child class
>>> miles = JackRussellTerrier("Miles", 4)
>>> buddy = Dachshund("Buddy", 9)
>>> jack = Bulldog("Jack", 3)

check if miles is also an instance of the parents class,Dog
>>> isinstance(miles, Dog)
True

change the speak method in child class
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
 
>>> miles = JackRussellTerrier("Miles", 4)
>>> miles.speak()
'Miles says Arf'
#can still change the sound by passing a parameter
>>> miles.speak("Grrr")
'Miles says Grrr'

using super() will refernce a method, speak(), in parent class and pass the variable of the child class 
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
        
