# "greedy cashier"
# a program that takes "change owed" as an input
# outputs the smallest amount of coins required to pay that change

from cs50 import get_float

#validate input
while True:
    #always prompt user for input first
    change = get_float("Change Owed: ")
    # if user input IS in range, break out of loop
    if change >= 0:
        print("success", change)
        break
    # elif change <= 0:
        # print("Int must be greater than 0")
        # change = get_float("Change Owed: ")
        # print("success", change)
        # break

