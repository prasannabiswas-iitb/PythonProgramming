/*
What Are Variables in C?

- Variables store data such as numbers, characters, or floating-point values.
- They have a type specifying what kind of data they store (e.g., 'int', 'char', 'float').
- Variables must be declared before use, specifying the type and the name, e.g., 'int age;'.

Rules for Variables in C

1. Naming Rules:
   - Variable names can contain letters (A-Z, a-z), digits (0-9), and underscores (_).
   - Names must start with a letter or underscore, not a digit.
   - Variable names cannot contain spaces or special characters other than underscore.
   - Names cannot be keywords or reserved words in C (like 'int', 'return').
   - Variable names are case-sensitive ('count', 'Count', and 'COUNT' are distinct).

2. Declaration and Initialization:
   - Variables must be declared with a type before use: 'data_type variable_name;'.
   - Multiple variables of the same type can be declared in one line: 'int x, y, z;'.
   - Variables can be initialized when declared: 'int x = 5;'.
   - If not initialized, variables hold garbage values until assigned explicitly.

int age;         // valid
float salary;    // valid
char initial;    // valid

int 2ndValue;    // invalid, starts with digit
int total$sum;   // invalid, special character
int return;      // invalid, keyword
int _count;      // valid, starts with underscore
*/


/*
<float.h>
float: %f, FLT_MIN, FLT_MAX
double: %lf, DBL_MIN, DBL_MAX
long double: %Lf, LDBL_MIN, LDBL_MAX

%e, %Le -> scientific notations
*/


/*
Mathematical Operations
*/