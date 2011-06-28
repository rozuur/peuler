/*
#define F(i,a) for(i=0;i<a;++i)
#define S(i) scanf("%d",&i)
main(){int n,i,j,x,h=900,t[h][h],s[h];S(n);F(x,n){S(h);F(i,h)F(j,i+1)S(t[i][j]);F(j,h)s[j]=t[i=h-1][j];while(i--)F(j,i+1)s[j]=t[i][j]+(s[j]>s[j+1]?s[j]:s[j+1]);printf("%d\n",s[0]);}return 0;}

*/

#define Z(a)scanf("%d",&a);
int r,b[101],i,j,m,o,p,z,y;
int main(){
for(Z(r)r--;){
  for(y=i=!Z(m)i++<m;)
    for(j=b[i]=o=0;j++<i&&Z(z))
      b[j]=((p=b[j])>o?b[j]:o)+z,o=p,b[j]>y&&(y=b[j]);
  printf("%d\n",y);
 }
 return 0;
}
