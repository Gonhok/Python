f4 = open('file2.txt','r')

for i in range(1,4):
	line = f4.readline()
	print(line[3*i:],end='')
#####
f4.seek(0,0)

count=0
for temp in range(3,10,3):
       f4.seek(count+temp,0)
       print(f4.readline(),end='')
       count = f4.seek(0,1)
       #seek의 리턴값은 현재의 포인터 값.
       #따라서 count를 현재위치로 업데이트 해준다.

f4.close()
