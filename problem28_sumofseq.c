/*
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Ans:

Clearly top right corner is odd power 
and all other corners are symetric around bottom right corner

so sum of corners in nth circle is  (2n+1)^2 + 3( (2n+1)^2 - 2*(2n+1 -1))

2n+1=1001  n=500
sum = sigma 4*(4*n*n+n+1)

*/
#include<stdio.h>
int main()
{
  unsigned int n,s=0;
  for(n=1;n<=500;++n)
    s+=4*(4*n*n+n+1);
  printf("%u",s+1);
}
