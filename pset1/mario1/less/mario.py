# program that takes an integer as an input
# and outputs a pyramid in mario form
# the pyramid has 'height' number of rows and the size of each row decreases by one at each step

from cs50 import get_int

while True:
    # always prompt user for input first
    height = get_int("Input integer for height: ")
    # if user input IS in range
    if height > 0 and height < 23:
        print("The height is: ", height)
        print("Here is the pyramid you asked for")
        break
    else:
        # reprompt the user
        print("Int must be between 0 and 23")
        height = get_int("Input integer for height: ")
        print("The height is: ", height)
        print("Here is the pyramid you asked for")
        break

# use for loop to print out this many rows (aka new lines \n)
# this will print as many rows as the user gives in int form
for i in range(height):
    # print spaces
    print(" ", end="")
    # print hashes
    print("#" * height)
    # print new line
    print()





