/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^(2) + b^(2) = c^(2)

For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Brute force 
*/

#include<stdio.h>
#include<math.h>

int main()
{
  int a,b;
  double c;

  for(a=1;a<1000;++a){
    for(b=1;b<1000 - (c=sqrt(a*a+b*b));++b){
      if( c == (int)c)
	if(a+b+c == 1000){
	  printf("%.0F\n",a*b*c);
	  return 0;
	}
    }
  }
  return 0;
}
