/*
main → returns int → C runtime → OS termination interface → kernel sets exit status → parent reads it.
*/

// #include<stdio.h>

// int main()
// {
//     printf("Hello World!");
//     return 0;
// }


/*
Type	                Bits (typical)	            Minimum	                    Maximum
signed char	                8	                       -128	                        127
unsigned char	            8	                        0	                        255
short	                    16	                       -32767-1	                    32767
unsigned short	            16	                        0	                        65535
int	                        32	                       -2147483647-1	            2147483647
unsigned int	            32	                        0	                        4294967295
long	                    32	                       -2147483647-1	            2147483647
unsigned long	            32	                        0	                        4294967295
long long	                64	                       -9223372036854775807-1	    9223372036854775807
unsigned long long	        64	                        0	                        18446744073709551615
*/

#include <stdio.h>
#include <limits.h>

int main()
{
    printf("================== Long Long ===========================\n");
    long long x;
    printf("Enter a number: \n");
    scanf("%lld", &x);
    printf("You entered %lld, Range: [%lld, %lld]", x, LLONG_MIN, LLONG_MAX);
    
    printf("================== Signed Char ===========================\n");
    signed char x1;
    printf("Enter a number: \n");
    scanf("%hhd", &x1);
    printf("You entered %hhd, Range: [%hhd, %hhd]", x1, SCHAR_MIN, SCHAR_MAX);
    return 0;
}

// int main()
// {
//     signed char x;
//     printf("Enter a number: \n");
//     scanf("%hhd", &x);
//     printf("You entered %hhd, Range: [%hhd, %hhd]", x+1, SCHAR_MIN, SCHAR_MAX);
//     return 0;
// }

// int main()
// {
//     unsigned char x;
//     printf("Enter a number: \n");
//     scanf("%hhu", &x);
//     printf("You entered %hhu, Range: [0, %hhu]", x, UCHAR_MAX);
//     return 0;
// }

/*
<limits.h>
singed char: %hhd, SCHAR_MIN, SCHAR_MAX
unsigned char: %hhu, UCHAR_MAX
short: %hd, SHRT_MIN, SHRT_MAX
unsigned short: %hu, USHRT_MAX
int: %d, INT_MIN, INT_MAX
unsigned int: %u, UINT_MAX
long: %ld, LONG_MIN, LONG_MAX
unsigned long: %lu, ULONG_MAX
long long: %lld, LLONG_MIN, LLONG_MAX
unsigned long long: %llu, ULLONG_MAX
*/