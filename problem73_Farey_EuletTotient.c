/*
How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d  12,000?

Ans : This is Farey's Sequence

Use this papers clever algorithm to find ranks of fractions  
http://www.math.harvard.edu/~corina/publications/farey.pdf

*/

#include<stdio.h>
int main()
{
  int t,n,den,i,j,out[2];
  t=2;
  while(t--){
    n=12000;
    int Farey[n+2];
    
    den = t==1? 2 : 3;

    for(i=0;i<=n;i++)
      Farey[i]=i/den;
    
    for(i=2;i<=(n>>1);i++){
      for(j=(i<<1);j<=n;j+=i){
	Farey[j]-=Farey[i];
      }
      Farey[i]+=Farey[i-1];
    }
    for(;i<=n;i++){
      Farey[i]+=Farey[i-1];
    }

    out[t]=Farey[n];
    printf("Rank of 1/%d is %d\n",den,Farey[n]+1);
  }
  printf("No of fractions in between are %d\n",out[1]-out[0]-1);
  return 0;
}

