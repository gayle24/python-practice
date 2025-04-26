#take in record of value which acts as limit
x = int(input("Input your value: "))
#set the base from which the factorial is calculated
fact = 1
#set restriction for negative numbers since their factorial is undefined
if x < 0:
    print("Factorial cannot be defined for negative numbers")
else:
    # set a range from 1 to the input value
    for i in range(1, x+1):
        #multiply the value of fact by the next number
        #then create a new value for fact
        fact *= i
    print("Factorial of", x ,"is", fact)