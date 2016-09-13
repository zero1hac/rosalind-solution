string = raw_input("Paste the given string here:")
a,b,c,d =  map(int,raw_input().split())
print a,b,c,d
print string[a:b+1], string[c:d+1]
