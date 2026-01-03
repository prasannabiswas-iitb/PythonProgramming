/*

# Lecture: Advanced Data Types in C

# 1. Why We Need Advanced Data Types

As programs grow more complex, we need:

* More compact ways of writing conditions → Ternary operator
* Custom names for existing types → typedef
* Named integer constants → enum
* Grouping multiple related values into a single unit → struct
* Handling multiple such units → arrays of structs

Before these features, code becomes:

* Too long
* Harder to maintain
* Repetitive
* Difficult to extend

Advanced data types give C programs structure, readability, and scalability.
*/

// Ternary Operator (`?:`)
// ===================================================================

// #include <stdio.h>

// int main()
// {
//   int a = 15, b = 10;
//   if(a<b)
//     printf("a is smaller\n");
//   else
//     printf("a is greater or equal");
//   return 0;
// }

// int main()
// {
//   int a = 5, b = 10;
//   (a<b) ? printf("a is smaller\n") : printf("a is greater or equal\n");
//   return 0;
// }


// ===================================================================

/*
### Explanation

`condition ? value_if_true : value_if_false`

### Why we use it

* Short, compact
* Good for simple decisions

### Limitations

* Not suitable for complex logic
* Harder to read when nested
  (avoid `(a>b ? (c>d ? x : y) : (e<f ? m : n))`)
*/


// ==================== 3. typedef — Giving New Names to Data Types
// ===================================================================

// ===================================================================
/*
### Why we use typedef

* Cleaner code
* Simplifies long types (e.g., pointers)
* Helps create readable APIs

### Limitations

* Can hide complexity
  Example:

typedef char* string;

Students may forget it’s actually a pointer.
*/

// ==================== 4. Enums (Enumerations)
// ===================================================================
// Enumerations give names to integer constants.

// ===================================================================

/*
### Why we use enums

* Increases readability
* Reduces accidental mistakes
* Group related constants

### Limitations

* Underlying values are still integers
* No type safety across enums in C
  (You can assign a value from another enum  — C doesn’t prevent it)
*/


// ==================== 5. Structs — Grouping Related Data
// ===================================================================
// Structures allow combining related data of different types.

// Before struct

// #include <stdio.h>

// int main()
// {
//     // char names[3][20] = {"Swaleha", "Hemanshi", "Kasturi"};
//     printf("Database of 3 students\n");
//     char names[3][20];
//     int age[3];
//     int marks[3];
//     for(int i=0; i<3; i++)
//     {
//         scanf("%s", names[i]);
//         scanf("%d", &age[i]);
//         scanf("%d", &marks[i]);
//     }

//     printf("Student Database\n");
//     for(int i=0; i<3; i++)
//         printf("%s - %d years old and got %d marks.\n", names[i], age[i], marks[i]);
//     return 0;
// }



// They are separate variables, not tied together.

// With struct

// #include <stdio.h>

// struct Student{
//   char name[20];
//   int age;
//   int marks;
// };

#include <stdio.h>

typedef struct{
  char name[20];
  int age;
  int marks;
} Student;

enum Grade {PASS, FAIL};

enum Grade fetch_result(Student s)
{
  if(s.marks < 40)
    return FAIL;
  return PASS;
}

int main()
{
    printf("Database of 3 students\n");
    Student students[4] = {{"Swaleha", 10, 55}, {"Hemanshi", 15, 89}, {"Kasturi", 25, 98}, {"rjkyt", 15, 30}}; 

    printf("Student Database\n");
    for(int i=0; i<4; i++)
        printf("%s - %d years old and got %d marks.\n", students[i].name, students[i].age, students[i].marks);

    printf("Student's result:\n");
    for(int i=0; i<4; i++)
    {
      enum Grade g = fetch_result(students[i]);
      if (g == PASS)
        printf("Congratulations %s\n", students[i].name);
      else
        printf("Try next time %s\n", students[i].name);
    }
    return 0;
}

// int main()
// {
//     struct Student students[3]; 
//     printf("Database of 3 students\n");
//     for(int i=0; i<3; i++)
//     {
//         scanf("%s", students[i].name);
//         scanf("%d", students[i].age);
//         scanf("%d", students[i].marks);
//     }

//     printf("Student Database\n");
//     for(int i=0; i<3; i++)
//         printf("%s - %d years old and got %d marks.\n", students[i].name, students[i].age, students[i].marks);
//     return 0;
// }


// ===================================================================
/*
### Why we use it

* Organizes data
* Makes programs scalable
* Basis for large systems and real-world models (students, cars, employees, etc.)

### Limitations

* Cannot contain functions (unlike C++)
* Assignment copies entire struct (may be costly)
* Memory layout depends on padding/alignment
*/

// ==================== 6. Arrays of Structs

// Used when we need to store multiple records.
// ===================================================================

// ===================================================================

/*
### Why we use arrays of structs

* Real-world datasets (lists of students, employees, books)
* Excellent for understanding memory layout
* Foundation for databases, files, and algorithms

### Limitations

* Fixed size (unless dynamically allocated)
* No bounds checking (C allows out-of-range access—dangerous)
* Updates and insertions are linear-time O(n)
*/


/*
# Mini Example Bringing All Topics Together


*/