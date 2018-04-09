#include <cs50.h>
#include <stdio.h>

// A program that reports a user’s water usage, converting minutes spent in the shower to bottles of drinking water.

// a program that prompts the user for the length of his or her shower in minutes (as a positive integer)
// and then prints the equivalent number of bottles of water (as an integer)

int main(void)
{
    int minutes; //initialize int

    //prompt the user for # of minutes until given positive integer
    do
    {
        minutes = get_int("# of minutes: ");
    }
    while(minutes < 0);

    printf("Bottles of Water Used: %i\n", minutes * 12);
    // print on a new line an int, the results of minutes * 12
}

