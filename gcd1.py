def gcd1(m,n):
	for i in reversed(range(1,min(m,n)+1)):
		if (m%i == 0) and (n%i == 0):
			return(i)


def gcd2(m,n):
	i=min(m,n)

	while i>0:
		if (m%i == 0) and (n%i == 0):
			return(i)
		else:
			i-=1


def gcd_list(m,n):

	fm=[]
	for i in range(1,m+1):
		if m%i == 0:
			fm.append(i)

	fn=[]
	for j in range(1,n+1):
		if n%j == 0:
			fn.append(j)

	cf=[]
	for f in fm:
		if f in fn:
			cf.append(f)

	return(cf[-1])



gcd_1=gcd1(9,12)
gcd_2=gcd2(9,12)
gcd_3=gcd_list(9,12)
print("gcd1={}\ngcd2={}\ngcd_list={}\n".format(gcd_1, gcd_2, gcd_3))