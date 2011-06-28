l = [200,100,50,20,10,5,2,1]
def f(n,k,l):
	if n<0:
		return 0
	if l[-1]==l[k] and n%l[-1] == 0 :
		return 1
	return f(n-l[k],k,l) + f(n,k+1,l)

if __name__ == "__main__":
	print f(200,0,l)

	# Dynamic Programming 
	n = 201
	l = [1,2,5,10,20,50,100,200]
	denom = [ [0]*n for i in xrange(len(l))]
	""" This makes only bindings
	similar to l=[0,0]
	a=[]
	a.append(l)
	a.append(l)
	both elements of a point to l, so any change in l is mirrored in both elements
	denom = [[0]*n]*len(l)
	"""

	for i in enumerate(denom[0]):
		if i[0]%l[0] == 0:
			denom[0][i[0]]=1
		else:
			denom[0][i[0]]=0

	for i in xrange(1,len(l)):
		if l[i]<n: 
			for j in xrange(l[i]): # From recursion count zero case
				denom[i][j]=denom[i-1][j]
		llist = range(l[i],n)
		for j in llist:
			denom[i][j] = denom[i][j-l[i]] + denom[i-1][j]
	#	print denom[i]
	print denom[-1][-1]
