/*

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Ans : Bruteforce ranging from  range ~ 900-999
		 
*/

#include<stdio.h>

int ispalindrome(char *s,int l)
{
  int i,j;
  for(i=0,j=l-1;s[i]==s[j];++i,--j);
  return (i>=j);
}

int main()
{
  int i,j,max;
  char s[7];

  max=1;
  for(i=999;i>900;--i){
    for(j=999;j>900;--j){
      sprintf(s,"%d",i*j);
      if( ispalindrome(s,6) == 1){
	if(i*j > max){
	  max = i*j;
	}
      }
    }
  }

  printf("%d\n",max);

return 0;
}
