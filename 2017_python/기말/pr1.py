m1=int(input())
d1=int(input())
m2=int(input())
d2=int(input())

md={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

result=0
for i in range(m1,m2):
    result += md[i]#달 사이 간격.

result += d2#뒤의 날짜를 더해준다.
result -= d1#앞의 날짜를 빼준다.
print('result: %d'%result)
