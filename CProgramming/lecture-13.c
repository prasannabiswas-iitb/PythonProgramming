/*
# Why We Need Arrays in C

### Problem Before Arrays

Suppose you want to store marks of 5 students.

### Code without arrays.
*/

// ===================================================================
// #include <stdio.h>

// int main()
// {
//     int m1 = 75;
//     int m2 = 86;
//     int m3 = 95;
//     printf("Marks = %d, %d, %d\n", m1, m2, m3);
//     return 0;
// }

// ===================================================================

/*
### Problems:

* Too many variables
* Hard to maintain
* No easy way to loop through values
* Not scalable
*/

/*
# Introduction to Arrays

An array stores multiple values of the same data type under one variable name.


### Syntax:

data_type array_name[size];
int marks[5] = {85, 90, 78, 88, 92};

### Accessing elements:
printf("%d", marks[0]); // first element


### Looping:
for (int i = 0; i < 5; i++) {
    printf("%d ", marks[i]);
}

### Limitations:

* Fixed size (cannot expand after creation)
* Must know size beforehand
* All elements must be same type
*/

// ===================================================================
// Example: Take 5 integers from user

// #include <stdio.h>

// int main()
// {
//     int numbers[5];
//     printf("Enter 5 integers\n");
//     for(int i=0; i<5; i++)
//     {
//         scanf("%d", &numbers[i]);
//     }
//     numbers[4]=50;
//     printf("You entered these numbers:\n");
//     for(int i=0; i<5; i++)
//     {
//         printf("%d\n", numbers[i]);
//     }
//     return 0;
// }


// ===================================================================

/*
A 2D array is like a table or matrix.

### Syntax:
int matrix[3][3];
int matrix[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};


### Limitations:

* Also fixed size
* Must know row and column sizes during creation
* Cannot return arrays directly from functions
*/
// ===================================================================
// #include <stdio.h>

// int main()
// {
//     int matrix[5][5];
//     int k = 100;
//     printf("Enter 5 integers\n");
//     for(int i=0; i<5; i++)
//     {
//         for(int j=0; j<5; j++)
//         {
//             matrix[i][j] = k;
//             k++;
//         }
//     }

//     printf("The numbers in the matrix are:\n");
//     matrix[3][4] = matrix[3][4]*100;
//     for(int i=0; i<5; i++)
//     {
//         for(int j=0; j<5; j++)
//         {
//             printf("%d ", matrix[i][j]);
//         }
//         printf("\n");
//     }
//     printf("%d ", matrix[4][3]);
    
//     return 0;
// }

// ===================================================================

/*
Before strings, you would need to do:
char c1 = 'a';
char c2 = 'b';
char c3 = 'c';
char c4 = 'd';
char c5 = 'e';

This is impossible for real words.

### Strings → array of characters ending with a NULL character (`\0`)

### Example:
char name[] = "abcde";

Equivalent to:
char name[] = {'a','b','c','d','e','\0'};

### Printing a string:
printf("%s", name);
*/
// ===================================================================


// ===================================================================

/*
# Arrays of Strings (2D char arrays)

Used to store multiple words.

### Example:
char names[3][20] = {
    "abcde",
    "xyz",
    "pqrs"
};



### Limitations:
* Each string must have fixed max length
* Memory is statically allocated
* Inflexible for variable-sized strings
*/
// ===================================================================
#include <stdio.h>

int main()
{
    // char names[3][20] = {"Swaleha", "Hemanshi", "Kasturi"};
    printf("Database of 3 students\n");
    char names[3][20];
    int age[3];
    for(int i=0; i<3; i++)
    {
        scanf("%s", names[i]);
        scanf("%d", &age[i]);
    }

    printf("Student Database\n");
    for(int i=0; i<3; i++)
        printf("%s - %d years old.\n", names[i], age[i]);
    return 0;
}
// ===================================================================



