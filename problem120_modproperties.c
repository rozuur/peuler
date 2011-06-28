/*
Let r be the remainder when (a−1)^(n) + (a+1)^(n) is divided by a^(2).

For example, if a = 7 and n = 3, then r = 42: 6^(3) + 8^(3) = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that r_(max) = 42.

For 3 ≤ a ≤ 1000, find ∑ r_(max).

Ans:

This was a very quick one: (a+1)^n == an+1 (mod a^2), and (a-1)^n == an-1 or 1-an (mod a^2) depending whether n is odd or even; the sum is therefore either 2an or 2.

When a is odd, this is always maximised at a^2-a (as in the example with a=7), achieved for example when n=(a-1)/2; when a is even, it is maximised at a^2-2a for a>2, achieved for example when n=(a-2)/2. 
*/

#include<stdio.h>
int main()
{
  int i,sum=0;
  for(i=3;i<=1000;++i){
    if(i&1){
      sum+= (i*i -i);
    }else{
      sum+=( i*i -(i<<1));
    }
  }
  printf("%d\n",sum);
}
