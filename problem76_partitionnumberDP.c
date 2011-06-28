/*
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
Ans : Its a partition function p

P(n,k) denotes the number of ways of writing n as a sum of exactly k
terms or, equivalently, the number of partitions into parts of which
the largest is exactly k. (Note that if "exactly k" is changed to "k
or fewer" and "largest is exactly k," is changed to "no element
greater than k," then the partition function q is obtained.) For
example, P(5,3)=2, since the partitions of 5 of length 3 are {3,1,1}
and {2,2,1}, and the partitions of 5 with maximum element 3 are {3,2}
and {3,1,1}.
 
Solved from recurrence relation
P(n,k) can be computed from the recurrence relation
P(n,k)=P(n-1,k-1)+P(n-k,k) 	
(55)

(Skiena 1990, p. 58; Ruskey) with P(n,k)=0 for k>n, P(n,n)=1, and P(n,0)=0.

Need to implement fast algo
http://www.numericana.com/answer/numbers.htm#partitions
 */

#include<stdio.h>

int main()
{
  int i,j;
  unsigned long long int a[102][102];

  a[1][1]=1;
  a[2][1]=1;a[2][2]=2;

  for(i=3;i<101;i++){
    a[i][1]=1;
    for(j=2;j<i;j++){
      if(j>i-j) 
	a[i][j]=a[i][j-1]+a[i-j][i-j];
      else 
	a[i][j]=a[i][j-1]+a[i-j][j];
    }
    a[i][i]=1+a[i][i-1];
  }

  printf("%li\n",a[100][100]-1);
  return 0;
}
