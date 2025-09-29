/*
A 'char' in C is used to store a single character (like 'a', 'Z', or '9').
A 'bool' is used to store logical values ('true' or 'false')
*/

/*

======================= Char in C =========================================

- A 'char' is a data type in C that stores a single character.  
- Internally, a 'char' is stored as an integer value based on the ASCII code of the character. For example, 'A' is stored as '65'.
- It takes 1 byte of memory in most systems.
- Used when you need to store characters (letters, symbols, digits treated as text).

*/


// Declaration and Definition


/*
Taking char as Input
%c -> char
*/


/*
Printing char
%c, %d -> ASCII value
*/


/*
Operations on char
- You can do arithmetic because chars are stored as ASCII integers.
*/


/*
====================== Bool in C =========================================
- In C99 onwards, we get a real boolean type using the header '<stdbool.h>'.  
- A boolean variable can be 'true' or 'false'.
*/


// Declaration and Definition

/*
Taking bool as Input
C does not have direct input for 'bool'. The usual way is:
- Take integer input (0 or 1). %d
- Assign to a boolean variable.
*/


/*
Printing bool
There is no direct '%b' format specifier, so we check with '%d' or print text for clarity.
bool x = true, y = false; "x = %d\n"
*/


/*
Operations on bool
- Logical operators work on 'bool': '&&' (AND), '||' (OR), '!' (NOT). 
*/ 