# Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.
def myfunction():
    print("Hello World")
    
# Arguments in Python Functions
def addNum(num1, num2):
    print(num1 + num2)


# Once we have defined a function, we can call it from another function, program, or even the Python prompt. 
# To call a function we simply type the function name with appropriate parameters.    
addNum(2, 4)

#In Python, you can use the return keyword to exit a function so it goes back to where it was called. 
# That is, send something out of the function.

def multiplyNum(num1):
    return num1 * 8



result = multiplyNum(8)
print(result)

# Output: 64