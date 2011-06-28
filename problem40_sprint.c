#define MAX 1000000
int main()
{
	char in[MAX+100],*p=in;
	int mod=10,pow=1,i=1;
	in[0]='0';
	while(1){
		if(p>in+MAX)
			break;
                p=p+pow;
		sprintf(p,"%d",i);
		if(i%mod == 0){
			pow=pow+1;
			mod*=10;
		}
                i++;
	}
	for(i=1;i<=MAX;i*=10) putchar(in[i]);
	return 0;
}
