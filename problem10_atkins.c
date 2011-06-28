/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define MAX 2000000
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
  int i,t,sq,n;
  char A[MAX]={0};

  /*
  printf("Enter number for which max factor need to be found : ");
  scanf("%llu",&n);
  putchar('\n');
  */

  n=MAX;
  sieveofatkins(A,n);

  unsigned long long int sum=0;
  for(i=n;--i;){
    if(A[i]==PRIME)
      sum+=i;
  }

  printf("Sum = %llu\n",sum);
  return 0;
}
