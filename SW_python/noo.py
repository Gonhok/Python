n = input().split()

count=0
for i in range(int(n[0]),int(n[1])+1):
    for j in str(i):
        if (j=='1'):
            count+=1
print (count)
