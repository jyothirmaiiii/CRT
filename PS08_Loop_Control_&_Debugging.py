'''
Docstring for Practice.S04.M01_Language_and_Programming.PS08_Loop_Control_&_Debugging
#Finding and Fixing of Errors called Debugging

#Types of Errors:
1) Syntax Errors--> Missing of Colon, Missing of indentation 
2) Run-Time Errors--> Any num is divisible by Zero 
3) Logical errors--> Missing of Logics 

#Debugging Techniques:
1) print() --> Run the code line by line 
2) try-except 
3) Using pdb

       Python Debugger:
         Main purpose is:
            1) To pause the Execution
            2) To run the codestep by step
            3) To inspect the variable's value

    pdb Commands:
        1) n --> execution in a next line
        2) p variable --> to print the value of a variable
        3) 1 --> List nearby code
        4) c --> To continue the Execution
        5) s --> Start with the function
        6) r --> return from the function
        7) h --> Help
        8) q --> Quit the Execution
'''
'''
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = a + b
print("value of a :", a)
print("value of b :", b)
print("Sum of a and b is :", c)

'''
'''
try:
    a=int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("Can not divisible by Zero")
except ValueError:
    print("Invalid input.")
'''

import pdb
def add(a,b):
    pdb.set_trace() #Setting a breakpoint for debugging
    return a+b
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(add(a,b))
