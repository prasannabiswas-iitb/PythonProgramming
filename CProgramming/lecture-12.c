/*
Mini Program: Menu-Based Loop Simulator

Students will write a program to show a menu repeatedly until they choose to exit.

This uses:
✔ while loop
✔ for loop
✔ break
✔ continue
✔ nested loops

Mini Project Code

*/

#include <stdio.h>

int main()
{
    printf("=============Loop Simulator=============");
    while(1)
    {
        printf("1. Press 1 for printing numbers 1 to N\n");
        printf("2. Press 2 for printing even numbers 1 to N\n");
        printf("3. Press 3 for Exiting....\n");

        int choice;
        scanf("%d", &choice);

        if(choice == 3)
            break;

        printf("Enter value of N\n");
        int N;
        scanf("%d", &N);

        if(choice == 1)
        {
            for(int i=1; i<=N; i++)
                printf("%d\n", i);
        }
        if(choice == 2)
        {
            for(int i=2; i<=N; i=i+2)
                printf("%d\n", i);
        }
    }
    return 0;
}