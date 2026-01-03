/*
1. 'math.h' Functions in C
#include <math.h>

1.1 'sqrt(x)' — Square Root
'double sqrt(double x);'
*/

// #include <stdio.h>
// #include <math.h>

// int main()
// {
//     double num = 64;
//     double sq_num = sqrt(num);
//     printf("Square root of %lf is %lf.", num, sq_num);
//     return 0;
// }



// #include <stdio.h>
// #include <math.h>

// int main()
// {
//     double base = 4;
//     double exponent = 3;
//     double pow_ = pow(base, exponent);
//     printf("Base %.1lf to power %.1lf is %.1lf.", base, exponent, pow_);
//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>
// #include <math.h>

// int main()
// {
//     int int_value = -100;
//     double float_value = -4.25;
//     printf("Abs value of %d = %d and Fabs value of %lf = %lf.", int_value, abs(int_value), float_value, fabs(float_value));
//     return 0;
// }


/*
1.2 'pow(x, y)' — Exponentiation
'double pow(double base, double exponent);'

1.3 'abs(x)' and 'fabs(x)' — Absolute Value

| Function         | Works On     | Header     | Returns |
| ---------------- | ------------ | ---------- | ------- |
| 'abs(int x)'     | int          | 'stdlib.h' | int     |
| 'fabs(double x)' | float/double | 'math.h'   | double  |


1.4 'round', 'ceil', 'floor'

| Function   | Description                                            |
| ---------- | ------------------------------------------------------ |
| 'round(x)' | Rounds to nearest integer (half values away from zero) |
| 'ceil(x)'  | Rounds upward to nearest integer                       |
| 'floor(x)' | Rounds downward to nearest integer                     |


1.5 Trigonometric Functions ('sin', 'cos', 'tan')
'double sin(double x);' (similarly 'cos()', 'tan()')

Arguments are in "radians", not degrees.

To convert degrees → radians:
double rad = angle * (M_PI / 180.0);
    
*/

// #include <stdio.h>
// #include <math.h>

// int main()
// {
//     double angle = 45;
//     double rad = angle * (3.14 / 180.0);
//     printf("Sin = %lf.", sin(rad));
//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>
// #include <math.h>

// int main()
// {
//     float x=3.2, y=3.2, z=3.5;
//     printf("Round(%lf) = %lf\n", x, round(x));
//     printf("Ceil(%lf) = %lf\n", y, ceil(y));
//     printf("Floor(%lf) = %lf\n", z, floor(z));
//     return 0;
// }

