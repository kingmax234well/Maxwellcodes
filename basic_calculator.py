def add(a, b):
    result = a + b
    print(str(a) + "+" + str(b) + "=" + str(result) + "\n")

def sub(a, b):
    result = a - b 
    print(str(a) + "-" + str(b) + "=" + str(result) + "\n") 

def mul(a, b):
    result = a * b
    print(str(a) + "*" + str(b) + "=" + str(result) + "\n")  

def div(a, b):
    result = a / b
    print(str(a) + "/" + str(b) + "=" + str(result) + "\n")

while True:
 print("A. Addition")
 print("B. Subtraction")
 print("C. Multiplication")
 print("D. Division")
 print("E. Exit")

 choice = input("Input your option: ")
 if choice == "a" or choice == "A":
     print("Addition")
     a = int(input("Input first number: "))
     b = int(input("Input second number: "))
     add(a, b)

 elif choice == "b" or choice  == "B":
     print("Subtraction")
     a = int(input("Input first number: "))
     b = int(input("Input second number: "))
     sub(a, b)

 elif choice == "c" or choice  == "C":
     print("Multiplication")
     a = int(input("Input first number: "))
     b = int(input("Input second number: "))
     mul(a, b)

 elif choice == "d" or choice  == "D":
     print("Division")
     a = int(input("Input first number: "))
     b = int(input("Input second number: "))
     div(a, b)

 elif choice == "e" or choice  == "E":
     print("Thanks for using our calculator app!")
     quit()

 else:
     print("Invalid input")

     
