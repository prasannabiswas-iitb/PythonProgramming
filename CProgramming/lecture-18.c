/*

# 1. Why We Need Dynamic Memory in C

### Before dynamic memory

Without dynamic memory, we write code like:

int arr[100];  // fixed size


Problems:
* Memory size is fixed at compile time.
* If we need more memory later, we are stuck.
* If we allocate too much “just in case,” memory gets wasted.

### With dynamic memory

We can decide at runtime how much memory we need:

int *arr = malloc(n * sizeof(int));
free(arr);
#include <stdlib.h>

Benefits:
* Flexible memory usage
* Useful when input size is unknown
* Allows large allocations on the heap
* Enables data structures like linked lists, trees, graphs

*/

// ==================== `malloc()`

//`malloc()` allocates a block of memory on the heap.
// void* malloc(size_t size);

// ===================================================================
// #include <stdio.h>
// #include <stdlib.h>

// int main()
// {
//   // int *arr = (int *)malloc(10 * sizeof(int));
//   int *arr = (int *)calloc(10, sizeof(int));
//   // for(int i=0; i<10; i++)
//   // {
//   //   arr[i] = i+1;
//   // }
//   for(int i=0; i<10; i++)
//   {
//     printf("Values at %d = %d\n", i, arr[i]);
//   }
//   free(arr);
//   return 0;
// }
// ===================================================================

/*
### Notes

* Memory is not initialized (contains garbage).
* Always check for `NULL`.
* Always `free()` after use.
*/

// ==================== `calloc()`

// `calloc()` allocates memory and initializes it to zero.
// void* calloc(size_t num, size_t size);

// ===================================================================

// ===================================================================

/*
### Differences from `malloc()`

| `malloc()`            | `calloc()`                    |
| --------------------- | ----------------------------- |
| Uninitialized memory  | Zero-initialized memory       |
| Slightly faster       | Slightly slower               |
| One argument (`size`) | Two arguments (`num`, `size`) |
*/


// ==================== `realloc()`

// `realloc()` changes the size of previously allocated memory.
// void* realloc(void* ptr, size_t new_size);

// ===================================================================
// #include <stdio.h>
// #include <stdlib.h>

// int main()
// {
//   int *arr1 = (int *)malloc(100 * sizeof(int));
//   for(int i=0; i<100; i++)
//   {
//     arr1[i] = i+1;
//   }
//   for(int i=0; i<100; i++)
//   {
//     printf("Values at %d = %d\n", i, arr1[i]);
//   }

//   arr1 = (int *)realloc(arr1, 105 * sizeof(int));
//   for(int i=100; i<105; i++)
//   {
//     arr1[i] = i+1;
//   }
//   for(int i=100; i<105; i++)
//   {
//     printf("Values at %d = %d\n", i, arr1[i]);
//   }
//   free(arr1);
//   return 0;
// }
// ===================================================================
/*
### Notes

* Keeps old data.
* May move memory to a new block.
* Must reassign:
  ptr = realloc(ptr, new_size);
*/

/*
# Common Limitations & Pitfalls

### Memory Leak
Forgetting to free memory:

int *p = malloc(100);  
// forgot free(p);


### Dangling Pointer
Using memory after free:

free(p);
printf("%d", *p);  // dangerous


### realloc() Pointer Loss

realloc(ptr, new_size);  // lost returned pointer

Correct:
ptr = realloc(ptr, new_size);


### Out-of-memory
Always check:

if (ptr == NULL) {
    // handle failure
}
*/

// ===================================================================

// #include <stdio.h>
// #include <stdlib.h>

// int main()
// {
//   printf("Enter size of array: \n");
//   int N;
//   scanf("%d", &N);
//   int *arr = (int *)malloc(N * sizeof(int));
//   for(int i=0; i<N; i++)
//   {
//     arr[i] = i+1;
//   }
//   for(int i=0; i<N; i++)
//   {
//     printf("Values at %d = %d\n", i, arr[i]);
//   }
//   free(arr);
//   return 0;
// }

// ===================================================================
