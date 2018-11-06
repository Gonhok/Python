str1 = input()

l1 = str1.split(' ')

f1 = open('file1.txt','w')

for temp in l1:
    f1.write(temp+'\n')

f1.close()
