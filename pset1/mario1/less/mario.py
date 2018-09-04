# program that takes an integer as an input
# and outputs a pyramid in mario form
# the pyramid has 'height' number of rows and the size of each row decreases by one at each step

from cs50 import get_int

while True:
    # always prompt user for input first
    height = get_int("Input integer for height: ")
    # if user input IS in range
    if height >= 0 and height <= 23:
        print("The height is: ", height)
        break
    elif height < 0 and height > 23:
        # reprompt the user
        print("Int must be between 0 and 23")
        height = get_int("Input integer for height: ")
        break

# for each loop iterates through height int
# ex/ 4 --> 1, 2, 3, 4
for i in range(height):
    # print spaces * (height - i)
    # print hashtags * (i + 2)
    print(" " * (height - i) + "#" * (i + 2))






