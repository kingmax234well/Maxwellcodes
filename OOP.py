# Object Oriented Programming in Python

#Creating a class
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)
#print(MyClass)


# The __init__ function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person("Maxwell", 36)
print(p2.name)
print(p2.age)        


# The __str__ function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
p3 = Person("Maxwell", 24)

print (p3)


#Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old")

p4 = Person("Maxwell", 78)

p4.myfunc()


# the self parameter
class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def myfunc(intro):
        print(f"Hello my name is {intro.name} and I am {intro.age} years old")

p5 = Person("Maxwell", 21)
p5.myfunc()