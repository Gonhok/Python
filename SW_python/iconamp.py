std = ['*x*',' xx','* *']

n = int(input())
for k in range(0,3):
    for i in range(0,n):
        for j in range(0,3):
            print(std[k][j]*n,end='')
        print()
