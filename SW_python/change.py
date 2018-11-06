money = int(input())

change=0
mm=(50000,10000,5000,1000,500,100,50,10)

for i in mm:
    change+=money//i
    money=money%i

print(change)

