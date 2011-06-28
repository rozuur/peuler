/*
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence: 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz
Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Ans:

http://en.wikipedia.org/wiki/Collatz_conjecture 

From here we can observe that highest step for numbers less than 1
billion is 670,617,279, with 986 steps.

We can use bitfields to define data structure for 10 bits unsigned
int.  This is done to fit 1 million numbers steps in array. If steps
are stored in int array it gives segfault

Observed this can be solved more fastly by using short :P
*/

#include<stdio.h>
#include<stdlib.h>
#define MAX 1000000

typedef struct _uint10{
  unsigned int i:10;
} uint10;

int collatz(uint10 *steps,int n)
{
  int count=0;
  unsigned long long int val=n;
  
  while(1){
    if(val<n && val<MAX){
      return (count+steps[val].i);
    }

    if(val&1 == 1){ // if val is odd
      val=((val<<1)+val+1)>>1;
      count+=2;
    }else{
      val=val>>1;
      ++count;
    }
  }
}

int main()
{
  int i,max,maxid,temp;
  uint10 steps[MAX]={0};

  steps[1].i=1;
  max=maxid=0;
  for(i=3;i<MAX;i+=2){
    steps[i-1].i=steps[(i-1)>>1].i;
    steps[i].i = collatz(steps,i);
    if(steps[i].i>max){
      max = steps[i].i;
      maxid=i;
    }
  }
  printf("%d:%d\n",max,maxid);
    
  return 0;
}
