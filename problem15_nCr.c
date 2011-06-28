/*
  40!/(20!*20!)
  21*23*25*..*39* 2^10 *11*12*..*19 / 20!
  21*23*25*..*39* 2^10 / 1*2*3*..*10
  <   10 terms  >

Using GMP
#include <gmp.h>
int main(){
	mpz_t n;
 	mpz_init(n);
	mpz_bin_uiui(n, 40, 20);
	gmp_printf("%Zd\n", n);
	return 0;
}
 */

#include<stdio.h>
typedef unsigned long long int uint64;

uint64 gcd(uint64 a,uint64 b){
  if(b==1)
    return 1;
  uint64 t;
  while(b){
    t=a;
    a=b;
    b=t%b;
  }
  return a;
}

int main()
{
  uint64 den,num,i,j,div;

  for(den=i=1;i<11;i++)
    den*=i;

  num=1;
  for(i=21;i<40;i+=2){
    num=num*i*2; // since 10 items are present and 2's power is 10
    div=gcd(num,den);
    num/=div;
    den/=div;
  }
  printf("%llu\n",num);
}
