/*
The first known prime found to exceed one million digits was
discovered in 1999, and is a Mersenne prime of the form 269725931; it
contains exactly 2,098,960 digits. Subsequently other Mersenne primes,
of the form 2p1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which
contains 2,357,207 digits: 28433*2^7830457+1.

Find the last ten digits of this prime number.

modular exponent
Ans: modular exponent 
(a+b)%n = a%n + b%n;
a*b % n = a%n * b%n;

It is observed that we cannot get last 10 digits of sum exactly using binary pow
But we can clearly get 9 digits ; so we can either trail and error or
implement using iterative mod pow

any way first digit of last 10 digits is 7

Theres an elegant sol at http://projecteuler.net/index.php?section=forum&id=48
need to implement it :)
*/

#include<stdio.h>
#define MOD 10000000000
#define ODD 1
#define MAX 1000
typedef unsigned long long int uint64;

uint64 modpow(int n,int pow,uint64 mod)
{
  uint64 base=n,ret=1;
  while(pow){
    if(pow & 1 == ODD){
      ret *= base;
      if(ret>=mod)
	ret%=mod;
    }
    pow>>=1;
    base *= base;
    if(base >= mod)
      base %= mod;
  }
  return ret;
}

uint64 iterativemodpow(int n,int pow,uint64 mod)
{
  int i;
  uint64 ret=1;

  if(pow&1){ // extract even power
    ret = n;
    pow = pow -1;
  }

  n = n*n; // since pow is always even we can multiply n^2 and iterate i by 2
  for(i=1;i<=pow;i+=2){
    ret *= n;
    if(ret >= mod)
      ret %= mod;
  }
  return ret;
}

int main()
{
  uint64 sum=0,i;

  sum = iterativemodpow(2,7830457,MOD);
  sum = (28433*sum+1)%MOD;
  
  printf("%llu\n",sum);
  return 0;
}
