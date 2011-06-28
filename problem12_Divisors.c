#include<stdio.h>
#include<math.h>

int divisors(int n)
{
  int i,c=0;
  for(i=2;i<sqrt(n);++i){
    if(!(n%i))
      ++c;
  }
  c = c<<1;
  if(i*i == n)
    ++c;
  return c+2;
}

int main()
{
  int i,n,d;
  d = 6;
  for(i=8;d<500;++i){
    n = (i*(i+1))>>1;
    if((n&1) == 0)
      d = divisors(n);
  }
  printf("Number = %d and Divisors = %d\n",n,d);
}
