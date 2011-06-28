/*
  http://www.math.harvard.edu/~corina/publications/farey.pdf
 */

#include<stdio.h>
#define MOD 10000000
#define MAX MOD/10

int main()
{
  int t,c=0,n,A,B,i,j,out[2]={0};
  long long int x;

  t=1;
  while(t--){
    n=MAX;
    int Farey[n+2];
    A=n-1;
    B=n;

    for(i=0;i<=n;i++){
      x=(long long int)i*A;
      x/=B;
      Farey[i]=x-Farey[1];
    }

    for(i=2;i<=(n>>1);i++){
      for(j=(i<<1);j<=n;j+=i){
	Farey[j]-=Farey[i];
      }
      out[1]=out[1]+Farey[i];
      c=out[1]/MOD;
      out[1]%=MOD;
      out[0]=out[0]+c;
    }

    for(;i<=n;i++){
      out[1]=out[1]+Farey[i];
      c=out[1]/MOD;
      out[1]%=MOD;
      out[0]=out[0]+c;
    }

    printf("Rank of %d/%d %d%d\n",A,B,out[0],out[1]);
  }
  return 0;
}
