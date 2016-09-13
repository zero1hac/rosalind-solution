a = int(raw_input("Enter a:"))
b = int(raw_input("Enter b:"))
total = 0
for i in range(a,b+1):
    if i%2!=0:
        total += i
print total
