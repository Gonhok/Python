def diffline(x1,y1,x2,y2):
    if x1 != x2 :
        m=(y2-y1)/(x2-x1)
        c=y1-m*x1
        return m,c
    else :
        return 0,0


a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1==a2:
	print('x=%d'%a1)
	
else:
	m,c = diffline(a1,b1,a2,b2)

	print('y=%8.2fx+%8.2f' %(m,c))
