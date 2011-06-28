/*
  1/x + 1/y = 1/n 
  x-n * y-n = n*n
 */
#include<stdio.h>
#include<math.h>

int divisors(int n)
{
  int i,c=0;
  for(i=2;i<n/2;++i){
    if(!(n%i))
      ++c;
  }
  if(n%i == 0)
    ++c;
  return c;
}

int main()
{
  int i,n,d;
  d = 6;
  for(i=8;d<1000;i+=2){
    if(i %1000 == 0)
    printf("Number = %d,Divisors = %d\n",i,d);
    n = (i*i);
    d = divisors(n);
  }
  printf("Number = %d and Divisors = %d\n",n,d);
}
