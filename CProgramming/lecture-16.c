/*
# Lecture: File Handling in C

## 1. Why We Need File Handling

Until now, your programs could only:

* Take input from the keyboard (using `scanf`)
* Display output to the screen (using `printf`)

But what if you want to:

* Save student marks permanently
* Write logs for a program
* Save settings or configurations
* Store sensor data
* Read large data files as input

Keyboard-only input/output is temporary → once the program ends, everything is gone.

File handling allows programs to store and retrieve data even after the program finishes.

*/

// ==================== How Programming Looked Before File Handling
// ===================================================================
// Example: storing student marks without files.

// #include <stdio.h>

// int main()
// {
//   char names[2][20];
//   int marks[2];
//   printf("Enter names of students\n");
//   scanf("%s", names[0]);
//   scanf("%s", names[1]);
//   printf("Enter marks of students\n");
//   scanf("%d", &marks[0]);
//   scanf("%d", &marks[1]);
//   printf("%s = %d and %s = %d", names[0], marks[0], names[1], marks[1]);
//   return 0;
// }


// ===================================================================

/*
If the program closes ⇒ data lost
Cannot save 100 or 1000 student records
Cannot load previously saved data

Hence → Files are required.
*/

/*
# Basics of File Handling

To work with files, C uses a special structure:
FILE *fp;


You open a file using `fopen()`:
fp = fopen("data.txt", "w");

You must close the file using:
fclose(fp);


# File Modes

| Mode   | Meaning                                         |
| ------ | ----------------------------------------------- |
| `"w"`  | Write (creates new file or overwrites existing) |
| `"a"`  | Append (writes at end of file)                  |
| `"r"`  | Read (file must exist)                          |
| `"w+"` | Read + Write (overwrite)                        |
| `"a+"` | Read + Append                                   |
| `"r+"` | Read + Write (file must exist)                  |

*/

/*
# Writing to Files (`fprintf`, `fputs`, `fputc`)

| Function  | Purpose         | Reads/Writes | Handles Spaces? | Best For              |
| --------- | --------------- | ------------ | --------------- | --------------------- |
| `fprintf` | formatted write | write        | yes             | writing variables     |
| `fputs`   | string write    | write        | yes             | writing sentences     |
| `fputc`   | char write      | write        | yes             | writing characters    |
| `fscanf`  | formatted read  | read         | no              | numbers, tokens       |
| `fgets`   | line read       | read         | yes             | full lines, sentences |
| `fgetc`   | char read       | read         | yes             | processing characters |


fprintf(fp, "xyz\n");
fputs("Computer Science\n", fp);
fputc('A', fp);
fgets(line, sizeof(line), fp)
(ch = fgetc(fp)) != EOF; putchar(ch)
fscanf(fp, "%s %d", name, &marks) != EOF
*/


// ===================================================================
// Example: Writing student names to a file
// #include <stdio.h>

int main()
{
  char names[2][20];
  int marks[2];
  FILE *fp;
  fp = fopen("student_data.txt", "w");

  printf("Enter names of students\n");
  scanf("%s", names[0]);
  scanf("%s", names[1]);
  printf("Enter marks of students\n");
  scanf("%d", &marks[0]);
  scanf("%d", &marks[1]);
  fprintf(fp, "%s = %d and %s = %d", names[0], marks[0], names[1], marks[1]);
  fclose(fp);
  return 0;
}


// ===================================================================
// Reading from Files (`fscanf`, `fgets`, `fgetc`)

// Example: Reading the file we wrote


// ===================================================================

// Character-by-Character Reading
#include <stdio.h>

int main()
{
  FILE *fp;
  fp = fopen("student_data.txt", "r");

  char line[200];
  while(fgets(line, sizeof(line), fp))
  {
    printf("%s", line);
  }
  fclose(fp);
  return 0;
}

// ===================================================================

/*
# Important Checks
Check if the file exists / opened properly

If `fopen` fails, it returns `NULL`.
Always close the file with `fclose`
Avoid writing to files opened in `"r"` mode

# Limitations of File Handling

| Limitation                           | Explanation                          |
| ------------------------------------ | ------------------------------------ |
| No error handling on corrupted files | Program may behave unpredictably     |
| File operations are slow             | Compared to memory operations        |
| Manual memory management             | Buffers must be sized correctly      |
| No automatic JSON/CSV/DB support     | Must implement manually              |
| Text files lose structure            | Binary files needed for complex data |
*/

