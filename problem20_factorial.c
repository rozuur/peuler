/*
n! means n  (n  1)  ...  3  2  1

Find the sum of the digits in the number 100

*/

#include<stdio.h>
#include<stdlib.h>
#define MAX 10000

int sumofdigits(int n)
{
  int sum=0;
  while(n){
    sum += (n%10);
    n/=10;
  }
  return sum;
}

int main()
{
  int i,j,c,t,n,len;
  int f[MAX]={0};

  /*
  printf("Enter a number for which factorial has to be found and <= %d\n",MAX);
  scanf("%d",&n);
  if(n>MAX)
    exit(EXIT_FAILURE);
  */
  n=100;

  f[0]=24;
  len=1;
  for(i=5;i<=n;++i){
    c=0;
    for(j=0;j<len;++j){
      t=f[j];
      t = c+t*i;
      f[j] = t % MAX;
      c = t / MAX;
    }

    if(c!=0){
      f[len]=c;
      len++;
    }
  }

  printf("Factorial, %d! = ",n);
  unsigned long long int sum=0;
  for(i=len-1;i>=0;--i){
    sum += sumofdigits(f[i]);
    printf("%d",f[i]);
  }

  printf("\nSum of digits in it are %llu\n",sum);
  return 0;
}
