/*

Program: Simple Scientific Calculator


*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// cos tan round floor fabs
int main()
{
    printf("===== Running Scientific Calc ======\n");
    printf("Enter 1. For sin\n");
    printf("Enter 2. For abs\n");
    printf("Enter 3. For ceil\n");

    int choice=0;
    scanf("%d", &choice);

    switch (choice)
    {
    case 1:
        printf("Enter angle in degrees:\n");
        double degree;
        scanf("%lf", &degree);
        double rad = degree * (3.14 / 180.0);
        printf("Sin = %lf.\n", sin(rad));
        break;

    case 2:
        printf("Enter integer number for abs:\n");
        int number;
        scanf("%d", &number);
        printf("Abs = %d.\n", abs(number));
        break;

    case 3:
        printf("Enter float number for ceil:\n");
        double number_;
        scanf("%lf", &number_);
        printf("Ceil = %lf.\n", ceil(number_));
        break;
    
    default:
        printf("Thanks for using our calculator. Give proper inputs.");
        break;
    }
    return 0;
}