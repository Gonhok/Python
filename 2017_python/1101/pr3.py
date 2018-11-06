f3 = open('file2.txt','w')

count=0
for i in range(1,31):
    f3.write('%3d'%i)
    count +=1
    #if (i%10==0):
    #   f3.write('\n')
    if count==10:
        count=0
        f3.write('\n')
f3.close()
