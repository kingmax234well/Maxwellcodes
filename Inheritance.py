# The parent class
# Inheritance allows us to define a class that inherits all the methods and properties from another class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("James", "Doe")
x.printname()

# The object class
class Student(Person):
    pass
x = Student("Mike", "Olsen")
x.printname()


#adding the __init__() function to a child class
class Student(Person):
    def __init__(self, fname, lname):
        #To prevent overidding the parent class__init__():
        Person.__init__(self, fname, lname)


# Implementing everything together
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Jason", "Statham")
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        self.graduationyear = 2023

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")

x = Student("Tom", "Holland")
x.printname()
x.welcome()


# Using the super() function to inherit all methods and properties from the parent class
class Person:
    def __init__(self, fname, lname, mname):
        self.firstname = fname
        self.lastname = lname
        self.middlename = mname
    def printname(self):
        print(self.firstname, self.lastname)    

class Student(Person): 
    def __init__(self, fname, lname, mname, year):
        super().__init__(fname, lname, mname)  # Using super() to call the parent class's __init__ method
        self.graduationyear = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.middlename} {self.lastname} to the class of {self.graduationyear}")

x = Student("Olua", "Kelechi", "Nathan", 2029)
x.printname()
x.welcome()