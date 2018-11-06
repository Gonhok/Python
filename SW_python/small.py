import math
n = int(input())

list=[]
for i in range(0,n):
    list.append(input().split())

mulist=[]
for i in list:
    for j in list:
        if (i==j):
            continue
        mulist.append(math.sqrt(pow((int(i[0])-int(j[0])),2)+pow((int(i[1])-int(j[1])),2)))

print('%.1f'%min(mulist))
