/*
Task for Students: Create a program with 2 options

1. Write student name + marks to a file
2. Read and display all records

*/
#include <stdio.h>

int main()
{
    printf("1. Press 1 to write data in a file.\n");
    printf("2. Press 2 to read data from a file.\n");
    int choice;
    scanf("%d", &choice);

    if(choice == 1)
    {
        FILE *fp;
        fp = fopen("student_data.txt", "a");
        printf("Enter data: (Student name, marks)");
        char name[20];
        int marks;
        scanf("%s", &name);
        scanf("%d", &marks);
        fprintf(fp, "%s = %d\n", name, marks);
        fprintf(fp, "\n");
        fclose(fp);
    }
    else
    {
        FILE *fp;
        fp = fopen("student_data.txt", "r");
        char line[200];
        while(fgets(line, sizeof(line), fp))
        {
            printf("%s", line);
        }
        fclose(fp);

    }
    return 0;
}

//     char names[2][20];
//     int marks[2];
//     FILE *fp;
//     fp = fopen("student_data.txt", "w");

//     printf("Enter names of students\n");
//     scanf("%s", names[0]);
//     scanf("%s", names[1]);
//     printf("Enter marks of students\n");
//     scanf("%d", &marks[0]);
//     scanf("%d", &marks[1]);
//     fprintf(fp, "%s = %d and %s = %d", names[0], marks[0], names[1], marks[1]);
//     fclose(fp);
//     return 0;
// }

// #include <stdio.h>

// int main()
// {
//     FILE *fp;
//     fp = fopen("student_data.txt", "r");

//     char line[200];
    // while(fgets(line, sizeof(line), fp))
    // {
    // printf("%s", line);
    // }
//     fclose(fp);
//     return 0;
// }