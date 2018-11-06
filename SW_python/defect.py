code = input()

sum=0
for i in code:
    sum+=int(i)

if(sum%7==4):
    print('Bad')
else:
    print('Good')
