class SBottle():
    water = 50

    def __init__(self,_water=50):
        self.water = _water

    def __add__(self,other):
        temp = SBottle()
        temp.water = self.water + other.water
        temp.water = temp.water*(3/4)
        return temp

class BBottle(SBottle):
    water = 250

    def __init__(self,_water=250):
        self.water = _water

    def __add__(self,other):
        temp = SBottle()
        temp.water = self.water + other.water
        temp.water = temp.water*(4/5)
        return temp
    
n = int(input())
m = int(input())

s1 = SBottle()
s2 = s1+s1#작은 물병2개
s3 = s1+s2#작은 물병3개

b1 = BBottle()
b2 = b1+b1#큰 물병2개
b3 = b1+b2#큰 물병3개

sbottle= divmod(n,3)
bbottle= divmod(m,3)

waterSum = 0
waterSum = s3.water*sbottle[0] + b3.water*bbottle[0]

if(sbottle[1] == 2):
    waterSum +=s2.water
elif (sbottle[1]==1):
    waterSum +=s1.water

if(bbottle[1] == 2):
    waterSum +=b2.water
elif (bbottle[1]==1):
    waterSum +=b1.water

print('sum of water : %.2f' %waterSum)
