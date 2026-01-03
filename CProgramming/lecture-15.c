/*
# Lecture: Pointers in C

## Why We Need Pointers in C

Pointers are one of the most powerful features of C, and they solve several important problems:

### Problem 1: Functions in C use *Pass by Value*

This means the function gets a copy of the variable, not the real one.
So if you try to modify a variable inside a function—it will not affect the original.

### Problem 2: Dynamic Memory

If you want to create variables or arrays at runtime, you need memory addresses.

### Problem 3: Arrays, Strings, Structures

All of these internally depend on pointers.
To understand C properly → you must understand pointers.

### Problem 4: Efficient Access

Pointers allow:

* direct memory access
* faster operations
* avoiding copying large data
*/

// ==================== What is a Pointer?

//A pointer is a variable that stores the address of another variable.

// Syntax:
// int *ptr;
// float *ptr1;

// Meaning:
// `ptr` is a pointer to an int. %p
// ===================================================================
// Example: Basic Pointer

// #include <stdio.h>

// int main()
// {
//   int x = 5;
//   int *ptr = &x;

//   printf("Value of x = %d\n", x);
//   printf("Addr of x (&x) = %p\n", &x);
//   printf("Value of ptr = %p\n", ptr);
//   printf("Value of x pointed by ptr = %d\n", *ptr);
//   return 0;
// }


// ===================================================================

/*
### Output Explanation:

* `x = 10`
* `&x` → memory address
* `p` → stores the address of `x`
* `*p` → value at the stored address, i.e., 10
*/


// ==================== Pass by Value (Default in C)

// Problem: Changes inside a function do *not* affect the original variable.
// ===================================================================

// #include <stdio.h>

// void increment(int n)
// {
//   n = n+1;
//   printf("Value of n (Inside Increment) = %d\n", n);
// }

// int main()
// {
//   int a = 5;
//   increment(a);
//   printf("Value of a (Inside main) = %d\n",a);
//   return 0;
// }

// ===================================================================

// ==================== Pass by Reference using Pointers

//We send the address to the function, so it can modify the original variable.
// ===================================================================
// #include <stdio.h>

// void increment(int *n)
// {
//   *n = *n+1;
//   printf("Value of n (Inside Increment) = %d\n", *n);
// }

// int main()
// {
//   int a = 5;
//   increment(&a);
//   printf("Value of a (Inside main) = %d\n",a);
//   return 0;
// }
// ===================================================================

/*
Pointer Diagram
// int x = 5;
// int *p = &x;
```
  x = 5          p → stores address of x
+-------+      +--------+
|   5   |      |&x=0xf45|
+-------+      +--------+
add=0xf45      add=0xf50
   x             p

*p dereferences p → gives value 5



# Pointer Use Cases

Updating variables inside functions
Dynamic memory (`malloc`, `calloc`, `realloc`)
Strings (char*)
Arrays (array name = pointer)
Structures (`struct Student *s`)
Faster parameter passing

*/

/*
# Limitations / Dangers of Pointers

| Issue              | Why it Happens                |
| ------------------ | ----------------------------- |
| Dangling Pointers  | Using freed memory            |
| Wild Pointers      | Uninitialized pointers        |
| Memory Leaks       | Forgetting to `free()` memory |
| Segmentation Fault | Accessing invalid memory      |
| Hard to Debug      | Errors happen at memory level |
*/

/*
### Good Practice:

Always initialize:

int *p = NULL;
*/

// ===================================================================
// Mini Program for Students (Pass by Value vs Reference)

// #include <stdio.h>

// void pass_by_value_square(int x)
// {
//   x = x*x;
// }

// void pass_by_ref_square(int *x)
// {
//   *x = (*x) * (*x);
// }

// int main()
// {
//   int n = 5;
//   pass_by_value_square(n);
//   printf("Square value (by value) = %d\n", n);
//   pass_by_ref_square(&n);
//   printf("Square value (by ref) = %d\n", n);
//   return 0;
// }


// ===================================================================