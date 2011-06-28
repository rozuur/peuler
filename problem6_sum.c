/*
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

(n(n+1)/2)^2 - n(n+1)(2n+1)/6 = n(n+1)/12 ( 3n*n + 3n - 4n -2)
                              = n(n+1)/12 ( 3n*n -n -2)
*/
#include<stdio.h>

typedef unsigned long long int uint64;
int main()
{
  int n;
  printf("Enter number : ");
  scanf("%d",&n);
  printf("%llu\n",(uint64) (n*(n+1)*(3*n*n -n -2))/12 );
  return 0;
}
