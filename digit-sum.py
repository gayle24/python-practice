#input the number as a string
digi = input("Enter your Number: ")
#add each value of the string to a list in integer format
digi_list = [int(x) for x in digi]
#sum the values of the list using sum function
digi_sum = sum(digi_list)
#display the final sum of the values of the digits
print("The sum of the consecutive values is:", digi_sum)
