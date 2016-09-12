n = input()
x = 0
y = 1
if n==0:
    print 0
elif n==1:
    print 1
else:
    while n-1>0:
        z = x + y
        x = y
        y = z
        n = n -1
    print z
