/*
Lecture: Loops and Control Flow in C

# 1. Why We Need Loops and Control Flow

### Before loops (the painful way)

Imagine printing numbers from 1 to 10 without loops:
*/

// ===================================================================
// #include <stdio.h>

// int main()
// {
//     printf("1\n");
//     printf("2\n");
//     printf("3\n");
//     printf("4\n");
//     printf("5\n");
//     return 0;
// }


// ===================================================================

/*
Problems:

* Repeated code
* Hard to maintain
* Impossible for large tasks (printing 1 to 10000)

### Why loops exist

Loops allow:

* Repetition of tasks
* Cleaner code
* Faster development
* Fewer mistakes
* Handling large-scale operations
*/

/*
# 2. while Loop

### Syntax

while (condition) {
    // code runs repeatedly
}

### Common mistake

If you forget i++, the loop runs forever → infinite loop.

### When to use `while`

* When you don’t know the number of iterations (ex: read until user enters -1).
*/

// ===================================================================
// Example: Print 1 to 5

// #include <stdio.h>

// int main()
// {
//     int i=1;
//     while(i<=100)
//     {
//         printf("%d\n", i);
//         i++;
//     }
//     return 0;
// }

// ===================================================================

/*
# 3. for Loop

### Syntax

for (initialization; condition; update) {
    // code
}

### When to use `for`

* When you know exactly how many iterations you need.
*/

// ===================================================================
// Example: Print even numbers from 2 to 10
// #include <stdio.h>

// int main()
// {
//     for(int i=2; i<=10; i=i+2)
//     {
//         printf("%d\n", i);
//     }
//     return 0;
// }

// ===================================================================


/*
# 4. break & continue

## break
Used to stop the loop immediately.

## continue
Skips the current iteration and moves to the next.
*/

// ===================================================================
// #include <stdio.h>

// int main()
// {
//     int i=1;
//     while(i<=10)
//     {
//         if(i==5)
//         {
//             i++;
//             continue;
//         }
//         printf("%d\n", i);
//         i++;
//     }
//     return 0;
// }

// ===================================================================


/*
# 5. Nested Loops

A loop inside another loop.
*/
// ===================================================================
// Example: Print a 3×3 star pattern
#include <stdio.h>

int main()
{
    for(int row=1; row<=3; row++)
    {
        for(int col=1; col<=3; col++)
        {
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}

// * * *
// * * *
// * * *

// ===================================================================
