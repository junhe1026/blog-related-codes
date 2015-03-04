def gcd(a,b):
	r = a % b
	if r == 0:
		print b
	else:
		gcd(b, r)
a = 98
b = 63
if a>b:
	gcd(a,b)
else:
	gcd(b,a)
