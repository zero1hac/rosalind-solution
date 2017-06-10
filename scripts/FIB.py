file1 = open('rosalind_fib.txt', 'r')
n, k = map(int, file1.readline().strip().split())
a, b = 0,1 
for i in xrange(1, n):
	a, b = b, k*a+b
print b
