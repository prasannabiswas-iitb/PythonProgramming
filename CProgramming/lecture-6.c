// Write a program to find area and perimeter of a rectange.
// Write a program to check if a character is a vowel.

#include <stdio.h>
#include <stdbool.h>

int main()
{
    // Problem-1
    printf("Program to calculate area and perimeter of a rectangle.\n");
    // Declare length, width, area, perimeter
    float length, width, area, perimeter;

    // Take length, width as input
    printf("Enter length: \n");
    scanf("%f", &length);
    printf("Enter width: \n");
    scanf("%f", &width);

    // Apply the formula
    area = length * width;
    perimeter = 2*(length+width);

    // Output the values
    printf("Area of rectange: %.2f\n", area);
    printf("Perimeter of rectange: %.2f\n", perimeter);

    // Problem-2
    printf("\nProgram to check if a character is a vowel. \n");
    // Declare a charcater
    char ch;

    // Take character as input
    printf("Enter a character (A-Z) (a-z): \n");
    scanf(" %c", &ch);

    // Apply the logic
    bool isVowel = (ch == 'a') || (ch == 'e') || (ch == 'i') || (ch == 'o') || (ch == 'u') || (ch == 'A') || (ch == 'E') || (ch == 'I') || (ch == 'O') || (ch == 'U');

    if(isVowel)
        printf("Character: %c is a Vowel.\n", ch);
    else
        printf("Character: %c is not a Vowel.\n", ch);

    return 0;
}


