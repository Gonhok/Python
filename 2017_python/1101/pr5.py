f1 = open('file3.txt','w')

for i in range (1,101):
    f1.write('%3d lines\n'%i)

f1.close()

os = int(input())


f2 = open('file3.txt','r')

s1= len(f2.readline())

os-=1
f2.seek(os*s1,0)
print(f2.readline(),end='')
