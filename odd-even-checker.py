#input your value
x = int(input("Enter your value x: "))
#using if-else statement to check if number is even or odd
#if remnant when divided by 2 is 0, then the number is indicated as even
if x % 2 == 0:
    print("The number is even")
#if not divisible by 2, the number is indicated as odd
else:
    print("The number is odd")