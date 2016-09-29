target = eval(input())

n = 0
nl = 0
m = 0
ml = 0

a = 1
b = 1
c = 1

ac = 0
bc = 0
cc = 0
while True:
	s = n & 7
	a = (n >> 3) & m
	b = (n >> (3 + ml)) & m
	c = (n >> (3 + 2 * ml)) & m
	
#	print('a={:d}, b={:d}, c={:d}'.format(a,b,c))
	
	ac = a * a * a 
	bc = b * b * b 
	cc = c * c * c 

	if s & 1 is 0:
		ac = ~ac + 1
	if s & 2 is 0:
		bc = ~bc + 1
	if s & 4 is 0:
		cc = ~cc + 1
	
	if ac + bc + cc is target:
		break
	else:
		n += 1
		if n & (n-1) is 0:
			nl += 1
			if nl % 3 is 0:
				ml += 1
				m = m * 2 + 1
			
			#print('a={:d}, b={:d}, c={:d}, n={:d}'.format(a,b,c,n))
		
if s & 1 is 0:
	a = ~a + 1
if s & 2 is 0:
	b = ~b + 1
if s & 4 is 0:
	c = ~c + 1
		
print('a={:d}, b={:d}, c={:d}'.format(a,b,c))