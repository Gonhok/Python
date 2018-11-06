f1 = open('t1.txt','w')

f1.write('이번 시간은 여기까지\n')#줄바꿈 문자 수동으로 넣어줘야한다.

for i in range(1,13):
    f1.write('%2d lines\n'%i)

f1.close()

f2= open('t1.txt','r')

for temp1 in f2:
#temp1 = f2.readlines()
#print(type(temp1))
    print(temp1,end='')#원래 파일에 개행있으므로 없애줌.

print('*'*20)#커서가 젤 뒤에있어서 더이상 못읽음->seek로 해결
f2.seek(2,0) #offset, location (0:start, 1:current, 2:end)

str1 = f2.read()
print(str1)
print('*'*20)


f2.close()
