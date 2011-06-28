/*
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
*/
#include<stdio.h>
#define MAX 1000

int main()
{

  int i,j,n,c,v,len,sum;
  char multi[2][10],carry[2][10];

  for(c=0;c<=1;c++)
  for(i=0;i<10;i++){
    multi[c][i] = (c+(i<<1))%10;
    carry[c][i] = (c+(i<<1))/10;
  }
  
  char num[MAX/3]={0};

  printf("Enter exponent of 2 : ");
  scanf("%d",&n);
  num[0]=1;
  len=1;
  for(i=0;i<n;i++){
    c=0;
    for(j=0;j<len;j++){
      v=num[j];
      num[j]=multi[c][v];
      c= carry[c][v];
    }
    num[j]=c;
    len+=c;
    /*
    printf("%d:%d ",i,n);
    for(j=0;j<n;j++)
      printf("%d",num[j]);
      puts("");
    */
  }

  printf("%d^%d ",i,n);
  sum=0;
  for(j=len-1;j>=0;--j){
    printf("%d",num[j]);
    sum+=num[j];
  }
  puts("");

  printf("Sum of 2^%d = %d\n",n,sum);
  
  return 0;
}
