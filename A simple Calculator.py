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
