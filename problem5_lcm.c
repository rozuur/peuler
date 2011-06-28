/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?

Find LCM(1,20)

*/
#include<stdio.h>
#include<stdlib.h>

int main(int argc,char **argv)
{
  printf("Please enter a number which is not greater than 60\n");
  int n;
  if(argc == 1)
    n=20;
  if(argc == 2)
    n = atoi(argv[1]);

  if(n>77) 
    exit(EXIT_FAILURE);

  unsigned long long int *LCM;
  LCM = malloc((n+1) * sizeof(*LCM));
  
  int i,j;
  for(i=1;i<=n;i++)
    LCM[i]=i;
  
  for(i=2;i<=(n/2);++i){
    if(LCM[i] != 1)
      for(j=i+i;j<=n ; j+=i){
	LCM[j]/=LCM[i];
      }
    LCM[i]=LCM[i-1]*LCM[i];
  }
  
  while(i<=n){
    LCM[i]=LCM[i-1]*LCM[i];
    i++;
  }

  /* 
  printf("LCM 's of numbers from 1 to i is\n"); 
  printf("i:lcm(1..i)\n");
  for(i=0;i<n;i++)
    printf("%d:%llu\n",i,LCM[i]);
  printf("\n");
  */
  
  printf("lcm of numbers from 1 to %d is %llu\n",n,LCM[n]);
  return 0;
}
