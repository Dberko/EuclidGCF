

def gcd(m, n):
	z = abs(m - n)
	if (m - n) == 0:
		return n
	else:
		return gcd(z,min(m,n))

a = int(input(">>"))
b = int(input(">>"))

print (gcd(a,b))