# A-simple-Calculator
Simple Working Calculator in Python
📌 Aim

To create a simple calculator program using Python functions that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

💻 Python Program
print("\n========== Working Simple Calc ==========\n")

def add(a,b):
    return a+b

def sub(a,b):
   return a-b

def mult(a,b):
   return a*b

def div(a,b):
   return a/b

while(True):

    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\n")

    choice=int(input("Enter your choice:"))

    if choice==1:
        a,b=map(float,input("Enter num1 and num2:").split())
        print(add(a,b),"\n")

    elif choice==2:
        a,b=map(float,input("Enter num1 and num2:").split())
        print(sub(a,b),"\n")

    elif choice==3:
        a,b=map(float,input("Enter num1 and num2:").split())
        print(mult(a,b),"\n")

    elif choice==4:
        a,b=map(float,input("Enter num1 and num2:").split())
        print(div(a,b),"\n")

    elif choice==5:
        print("EXIT SUCCESSFUL")
        break

    else:
        print("INVALID CHOICE!\n")
▶️ Sample Output
========== Working Simple Calc ==========

1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit

Enter your choice:1
Enter num1 and num2:10 20
30.0

Enter your choice:3
Enter num1 and num2:5 4
20.0

Enter your choice:5
EXIT SUCCESSFUL
🧠 Explanation
Functions are created for each arithmetic operation:
add() → Addition
sub() → Subtraction
mult() → Multiplication
div() → Division
The while(True) loop keeps the calculator running until the user selects Exit.
The user selects an operation using menu choices.
map(float, input().split()) is used to take two numbers in a single line.
Based on the user's choice, the corresponding function is called and the result is displayed.
📚 Concepts Used
Functions
Infinite while loop
Conditional statements (if-elif-else)
User input
Arithmetic operators
break statement
map() function
