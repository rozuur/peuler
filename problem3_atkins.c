/*The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number n = 600851475143 ?
                                                         __ 
Ans : First find all primes using sieve of atkins till \/ n

And iterate from max prime to find factor

*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define MAX 800000
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
  int i,t,sq;
  char A[MAX]={0};
  unsigned long long int n;

  printf("Enter number for which max factor need to be found : ");
  scanf("%llu",&n);
  putchar('\n');

  sq = sqrt(n);
  sieveofatkins(A,sq);

  for(i=sq;--i;){
    if(A[i] == PRIME && n%i == 0){
      printf("%d\n",i);
    }
  }

  return 0;
}
