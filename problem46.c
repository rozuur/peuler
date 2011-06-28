// No need to generate primes also blind brute force gets accepted
// Just iterate through 2 to sqrt(n) and determine n is prime or not
#include <stdio.h>
#include <stdlib.h>
#include<math.h>

#define MAX 10000
#define ISPRIME(n) (A[n]==PRIME)
enum {COMPOSITE=0,PRIME=1};
int A[MAX+10];

int sieveofatkins(int num)
{
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
 
int conjectureIsTrue (int odd)
{
  int square;
  for (square=0; 2*square*square < odd; square++)
    {
      if (ISPRIME(odd-2*square*square))
	return 1;
    }
  return 0;
}
 
int main (){
  sieveofatkins(MAX);
  int odd=35;
  while (conjectureIsTrue(odd))
    odd+=2;
  printf("%d\n",odd);
  return 0;
}
