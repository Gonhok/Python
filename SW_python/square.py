           
def squre(list,x,y,lenlist):
    c=[0,0]
    ss=0
    for i in range(x,x+lenlist):
        for j in range(y,y+lenlist):
            ss+=int(list[i,j])
    if(ss==pow(lenlist,2)):
        c[1]+=1
        return c
    elif(ss==0):
        c[0]+=1
        return c
    else:
        a=squre(list,x,y,lenlist//2)
        c[0]+=a[0]
        c[1]+=a[1]
        a=squre(list,lenlist//2,y,lenlist//2)
        c[0]+=a[0]
        c[1]+=a[1]
        a=squre(list,x,lenlist//2,lenlist//2)
        c[0]+=a[0]
        c[1]+=a[1]
        a=squre(list,lenlist//2,lenlist//2,lenlist//2)
        c[0]+=a[0]
        c[1]+=a[1]


n= int(input())
list=[i for i in range(0,n)]
for i in range(0,n):
    k=input().split()
    list[i]=k
c=squre(list,0,0,n)
print(c[0])
print(c[1])
