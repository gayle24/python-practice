#function to reverse string
def reverse_string():
    #take in input string to be reversed
    inp = input("Enter a word to be reversed: ")
    #initialize an empty string where the reverse will be stored
    oup = ""

    #for loop to loop through letter of input from the end
    for letter in inp:
        oup = letter + oup
    # return the final reversed output
    return oup
#call function
print(reverse_string())