k,n=input().split()

rem=int(k)
n=int(n)
cof=0

while(rem//n):
    cof+=rem//n
    rem=(rem%n+rem//n)
    
print(cof)
