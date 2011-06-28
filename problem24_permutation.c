/*
A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2,
3, 4, 5, 6, 7, 8 and 9?

*/

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define NTHTERM 1000000

void swapdisplay(char *a,int i,int j) 
{ //prints "a" only is a[i] != a[j] this ensures dupes are not formed
  static count=1;
  if(a[i]^a[j]){ // a[i] not equal to a[j]
    char t;
    t=a[i];
    a[i]=a[j];
    a[j]=t;
    ++count;
   
    if(count == NTHTERM){
      printf("Lexicographic order of sequence %s is %d\n",a,count);
      exit(EXIT_SUCCESS);
    }
    
  }
}

int printpermute(char *A,int start,int end)
{ 
  int i,j;
  char *p;
  for(i=start;i<end;i++){
    swapdisplay(A,start,i); // displays first min's 1234,2134,3124,4123
    //now for each first min move start and find permutations(first mins)
    
    p=strdup(A);  // retention of A is possible by passing a copy of A
    printpermute(p,start+1,end);
    free(p);
  }

}

int main(int argc,char **argv)
{
  if(argc!=2)
    return(printf("Error"));
  printf("Permuter %s\n",argv[1]);
  printpermute(argv[1],0,strlen(argv[1]));
}
