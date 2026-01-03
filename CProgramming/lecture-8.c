/*
2. Decision Making in C

2.1 'if-else' Statement
if (condition) {
    ...
} else {
    ...
}
    */
#include <stdio.h>
int main()
{
    int age = 14;
    if(age >= 18)
    {
        printf("You can vote.");
    }
    else
    {
        printf("You can not vote.");
    }
    return 0;
}

/*
=====



2.2 Nested 'if' Statements

=====



2.3 'else if' Ladder

=====
#include <stdio.h>
int main()
{
    int marks = 95;
    if(marks >= 90)
        printf("Grade A.");
    else if(marks >= 75)
        printf("Grade B.");
    else if(marks >= 60)
        printf("Grade C.");
    else if(marks >= 50)
        printf("Grade D.");
    else
        printf("Grade E.");
    return 0;
}

=====


3. 'switch' Statement

Used when comparing one variable against multiple constant values.

=====


Only works with integer and character constants (not floating values).
Must use 'break' to prevent fall-through.
=====
#include <stdio.h>
int main()
{
    int choice = 1;
    switch(choice)
    {
        case 1: printf("One"); printf("%d", choice); break; 
        case 2: printf("Two"); break;
        case 3: printf("Three"); break;
        case 4: printf("Four"); break;
        case 5: printf("Five"); break;
        default: printf("Done!!!");
    }
}
===============================*************=========================

4. Logical Operators

| Operator | Meaning     | Example  | Result                 |    |   |    |                         |
| -------- | ----------- | -------- | ---------------------- | -- | - | -- | ----------------------- |
| '&&'     | Logical AND | 'x && y' | True only if both true |    |   |    |                         |
| '        |             | '        | Logical OR             | 'x |   | y' | True if any one is true |
| '!'      | Logical NOT | '!x'     | Reverses truth value   |    |   |    |                         |



*/
