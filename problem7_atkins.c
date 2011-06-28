/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

Ans :

from http://primes.utm.edu/howmany.shtml
 
pi(x) no of primes

x       pi(x) 
10	4	 
100	25	 
1,000	168	 
10,000	1,229	 
100,000	9,592	 

*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define MAX 200000
enum {COMPOSITE=0,PRIME=1};

int sieveofatkins(char* A,int num)
{
  printf("Find primes till number %d\n",num);
  int i,j,x,y,n,zeros,sq=sqrt(num);


  for(x=1;x<=sq;x++){
    for(y=1;y<=sq;y++){

      n=x*x*4+y*y;
      if(n<=num && (n%12 ==1 || n%12 == 5))
	A[n]= !A[n];

      n=3*x*x+y*y;
      if(n<=num && n%12==7)
	A[n]=  !A[n];

      n=3*x*x-y*y;
      if(x>y && n<=num && n%12 == 11)
	A[n]= !A[n];

    }
  }

  for(i=5;i<=sq;i++){
    if(A[i]==PRIME){
      n=i*i;
      for(j=n;j<=num;j+=n)
	A[j]=COMPOSITE;
    }
  }

  A[2]=A[3]=PRIME;
  A[1]=A[0]=COMPOSITE;
}

int main(void)
{
  int i,j,t,sq,n;
  char A[MAX]={0};

  /*
  printf("Enter number for which max factor need to be found : ");
  scanf("%llu",&n);
  putchar('\n');
  */

  n=MAX;
  sieveofatkins(A,n);

  unsigned long long int sum=0;
  j=0;
  for(i=0;i<n;i++){
    if(A[i]==PRIME)
      j++;
    if(j==10001){
      printf("%d\n",i);
      break;
    }
  }

  return 0;
}
