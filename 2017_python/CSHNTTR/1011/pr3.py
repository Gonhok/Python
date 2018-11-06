for i in range(9,0,-1):
    for j in range(1,8):
        if i==8 or i==7 or i==6 or i==5:
            if j==6 or j==7:
                continue
        print('%4d'%(100*i+j),end='')
    print()
