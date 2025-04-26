#import factorial for computing from math library
from math import factorial
#define function to compute factorial,
# takes in an integer variable
def fact_function(x):
    #set restrictions for negative numbers and input=0
    if x<0:
        return "Factorial only defined for non-negative numbers"
    elif x == 0:
        return 1
    #use factorial() to calculate the factorial of positive integers
    else:
        return factorial(x)
#take in user input of an integer value
num = int(input("Enter your numerical value:"))
#display factorial of integer by calling fact_function()
print("The factorial of", num, "is:",fact_function(num))