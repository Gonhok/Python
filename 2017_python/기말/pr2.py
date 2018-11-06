n = int(input())
sum=0

for i in range(1,n+1):
    if(i%2):
        sum += i
    else:
        sum -= i

print('result: %d'%sum)
