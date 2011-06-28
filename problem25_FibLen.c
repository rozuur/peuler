/*
Saying that a number contains 1000 digits is the same as 
saying that it's greater than 10**999. 

The nth Fibonacci number is [phi**n / sqrt(5)], where the 
brackets denote "nearest integer". 

So we need phi**n/sqrt(5) > 10**999 

n * log(phi) - log(5)/2 > 999 * log(10) 

n * log(phi) > 999 * log(10) + log(5)/2 
n > (999 * log(10) + log(5) / 2) / log(phi) 

 */
#include<stdio.h>
#include<math.h>

#define  phi ((1 + sqrt(5))/2)
#define  logsqrt5 (log10(sqrt(5)))
#define  logphi (log10(phi))

int main()
{
  printf("%.0F\n",ceil( (1000-1+logsqrt5)/logphi));
}
