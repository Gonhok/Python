str1 = 'abc'
l1=[9,7,5,3,1]
d1={1:'a',2:'b'}

for i in str1:
    print(i)
for j in l1:
    print(j)
for k in d1.values():
    print(k)


print("*"*10)
for i in range(5):
    print(i)
for j in range(1,10):
    print(j)
for k in range(1,10,2):
    print(k)
    
print("*"*10)
x=5
while x<10:
    print(x)
    x+=1

print("*"*10)
menu=0
#while menu!=3:

    #print('1')
    #print('2')
    #print('3')

#    menu = int(input('select menu: '))

print("*"*10)
l1=[]

for i in range(1,6):#1
    if i%2==0:#2
        l1.append(i)#3

l2 = [j for j in range(1,6) if j%2==0] #3 #1 #2

print(l1)
print(l2)

print([j for j in range(1,3) for i in range(1,3)])#???

print("*"*10)
for j in range(9,0,-1):
    for i in range(3,10,2):
        print('|%d*%d=%2d|'%(i,j,i*j),end='')
    print()

for i in range(1,10):
    if i==3:
        continue
    if i==7:
        break
    print('#',i)
