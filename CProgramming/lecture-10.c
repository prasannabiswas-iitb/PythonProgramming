/*
Functions in C

Why Do We Need Functions?

### Problems *before* functions:

Without functions, the entire program is inside `main()`.
This leads to:

* Repetitive code
* Hard to read
* Hard to debug
* No reusability
* No modularity

### Example: Code without functions

We calculate area of multiple circles, but we write the same formula again and again.
*/
// ===================================================================
// #include <stdio.h>

// int main()
// {
//     float r1 = 3.5;
//     float r2 = 5.0;

//     float area1 = 3.143 * r1 * r1;
//     float area2 = 3.143 * r2 * r2;

//     printf("Area of first circle = %.2f\n", area1);
//     printf("Area of second circle = %.2f\n", area2);
//     return 0;
// }

// ===================================================================
/*
### What’s wrong here?

* Formula repeated
* If formula changes → change everywhere
* `main()` becomes large and unreadable
*/

/*
# What Are Functions?

A function is a block of code that performs a specific task.

### Benefits:

* Modular – break program into smaller units
* Reusable – write once, use many times
* Readable – program is organized
* Easy to test and debug


# Writing Functions (Function Definition)
*/
// ===================================================================


// return_type function_name(parameters) {
//     // function body
//     return value;   // optional
// }

// #include <stdio.h>

// void greet()
// {
//     printf("Welcome Students!!!!");
// }

// int main()
// {
//     // greet();
//     return 0;
// }


// ===================================================================


/*
# Return Values in Functions

Functions can return values using `return`.

### Why return values?

* Useful when function needs to send data back to caller
* Makes function reusable for different values

### Example: Adding two numbers
*/
// ===================================================================

// #include <stdio.h>

// int add_num(int x, int y)
// {
//     int result = x+y;
//     return result;
// }

// float area(float radius)
// {
//     float area_ = 3.143 * radius * radius;
//     return area_;
// }

// int main()
// {
//     float r1 = 3.5, r2 = 5, r3 = 10;
//     float area1 = area(r1);
//     float area2 = area(r2);
//     float area3 = area(r3);
//     printf("Area1 = %.2f\n Area2 = %.2f\n, Area3 = %.2f\n", area1, area2, area3);
//     // int a = 10, b = 10;
//     // int res = add_num(a, b);
//     // printf("Addition = %d\n", res);
//     return 0;
// }

// ===================================================================


/*
# Variable Scope in C

Scope means where a variable is accessible.

---

## 5.1 Local Variables

✔ Declared inside a function
✔ Accessible only within that function

## 5.2 Global Variables

✔ Declared outside all functions
✔ Accessible in all functions

### Limitation of global variables:

* Too many globals → hard to track
* Code becomes less modular
* In large projects, globals cause bugs
*/

// ===================================================================
// #include <stdio.h>

// int global_var = 3;

// int add_num(int x, int y)
// {
//     int result = x+y;
//     printf("Local var = %d\n", result);
//     printf("Global var = %d\n", global_var);
//     return result;
// }

// float area(float radius)
// {
//     float area_ = 3.143 * radius * radius;
//     printf("Local var =  %.2f\n", area_);
//     printf("Global var = %d\n", global_var);
//     return area_;
// }

// int main()
// {
//     float r1 = 3.5, r2 = 5, r3 = 10;
//     float area1 = area(r1);
//     float area2 = area(r2);
//     float area3 = area(r3);
//     printf("Area1 = %.2f\n Area2 = %.2f\n, Area3 = %.2f\n", area1, area2, area3);
//     int a = 10, b = 10;
//     int res = add_num(a, b);
//     printf("Addition = %d\n", res);
//     printf("Global var = %d\n", global_var);
//     return 0;
// }

// ===================================================================


/*
# Function Prototypes

A function prototype tells the compiler:

> “This function exists, and this is what it looks like.”

### Needed because:

* C reads from top to bottom
* If a function is called before being defined, compiler gives a warning/error

### Why use prototypes?

* Avoids compilation issues
* Allows functions to be defined after main()
* Helps compiler catch mistakes in parameters
*/

// ===================================================================
#include <stdio.h>

int global_var = 3;

int add_num(int x, int y);
float area(float radius);

int main()
{
    float r1 = 3.5, r2 = 5, r3 = 10;
    float area1 = area(r1);
    float area2 = area(r2);
    float area3 = area(r3);
    printf("Area1 = %.2f\n Area2 = %.2f\n, Area3 = %.2f\n", area1, area2, area3);
    int a = 10, b = 10;
    int res = add_num(a, b);
    printf("Addition = %d\n", res);
    printf("Global var = %d\n", global_var);
    return 0;
}

int add_num(int x, int y)
{
    int result = x+y;
    printf("Local var = %d\n", result);
    printf("Global var = %d\n", global_var);
    return result;
}

float area(float radius)
{
    float area_ = 3.143 * radius * radius;
    printf("Local var =  %.2f\n", area_);
    printf("Global var = %d\n", global_var);
    return area_;
}


// ===================================================================

/*
# Limitations of Functions in C

| Limitation                  | Explanation                                      |
| --------------------------- | ------------------------------------------------ |
| No default arguments        | Unlike C++ or Python                             |
| No function overloading     | Same name cannot be reused with different params |
| No nested functions (ISO C) | Functions cannot be defined inside functions     |
| Must manage prototypes      | Without them, compiler may assume wrong details  |
*/