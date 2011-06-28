/*If we list all the natural numbers below 10 that are multiples of 3
  or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.  

Ans : Using Arithmetic progression

  a+(n-1)*d = l 
  n-1 = l-a / d
  a is first term ,d is diff ; l is last and n no of terms

  sum of terms of {3,6,9,..} + {5,10,15,...} - {15,30,...}

*/

#include<stdio.h>

inline int noofterms(int a,int d,int l)
{
  return (1+((l-a)/d));
}

inline int sumofterms(int a,int d,int n)
{
  return (n*(2*a + (n-1)*d)/2);
}

int main()
{
  printf("%d\n",						\
	 sumofterms(3,3,noofterms(3,3,1000-1)) +		\
	 sumofterms(5,5,noofterms(5,5,1000-1)) -		\
	 sumofterms(15,15,noofterms(15,15,1000-1))		\
	 );
}

