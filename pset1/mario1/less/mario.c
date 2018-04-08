#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //initialize i
    int height;
    //do-while loop always runs at least once
    do
    {
        //prompt user for an integer
        height = get_int("Height: ");
    }

    //do that for when the integer is (< 0 or > 23) --> "invalid"
    while (height < 0 || height > 23);

     // for loop iterates through ROWS which is the height
     // contains 2 nested routes
    for (int row = 0; row < height; row++)
    { //for loop to create correct amount of spaces for given# of bricks
        for (int space = 0; space < height - row -  1; space++)
        {
            printf(" ");
        } // for loop to create correct # of hashes
        for (int hashes = 0; hashes < row + 2; hashes++)
        {
            printf("#");
        } //to put in the proper line breaks after each loop
        printf("\n");
    }
}


