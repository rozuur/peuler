/*
A triplet of positive integers (a,b,c) is called a Cardano Triplet if it satisfies the condition:

For example, (2,1,5) is a Cardano Triplet.

There exist 149 Cardano Triplets for which a+b+c ¡Ü 1000.

Find how many Cardano Triplets exist such that a+b+c ¡Ü 110,000,000.

Note: This problem has been changed recently, please check that you are using the right parameters.

Ans :
 x+y=1
 (x+y)^3 = 1 => x^3 + y^3 + 3xy = 1
 
 solving (2a-1/3)^3 = b*b*c - a*a
  a = 2,5,8,11 ..
  k = 2a-1/3 = 1,3,5,7 ..

a+b+c<=M
b*b*c<=b*b*(M-a-b)
k*k*k+a*a<=b*b(M-a-b)<=b*b(M-a)
b*b>=k*k*k+a*a/M-a
*/

#include<stdio.h>
#include<math.h>
#define MAX 110000000
typedef unsigned long long int uint;

int main()
{
  uint a,b,c,k,count=0;

  for(a=2,k=1;a<=MAX;a+=3,k+=2){ // k = 2a-1/3
    printf("a = %llu\n",a);
    b = sqrt((k*k*k+a*a)/(MAX-a));
    for(;(a+b)<=MAX;++b){
      for(c=1;(a+b+c)<=MAX && b*b*c-a*a<=k*k*k;++c){
	if(k*k*k == b*b*c-a*a){
	  count++;
	 // printf("%llu %llu %llu %llu\n",a,b,c,count);
	}	
      }
    }
  }

  printf("%llu\n",count);
  return 0;
}
