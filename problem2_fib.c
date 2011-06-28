/*
  
1 1 (2) 3 5 (8) 13 21
x y (x+y) x+2y 2x+3y (3x+5y)
 */
#include<stdio.h>
#define MAX 1000000

int main()
{
  int x,y,t,s;
  x=y=1;
  s=0;
  while(x+y<MAX){
    s+=(x+y);
    t=x;
    x=t+2*y;
    y=2*t+3*y;
  }
  printf("%d\n",s);
  return 0;
}
