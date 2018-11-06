b = int(input())
s = int(input())

gcd = 1

while(1):
    if b%s==0:
        gcd = s
        break
    else:
        s,b = b%s,s
print(gcd)
