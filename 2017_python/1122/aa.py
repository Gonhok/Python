class Car:
    tire = 4
    man = 4
    def __init__(self, _tire=4, _man=4):
        self.tire = _tire
        self.man = _man
    def __del__(self):
        print('del')
    def run(self):#스스로 달리므로 self반드시 넣어야함.
        print('na dalinda')

    def stop(self):
        print('na meomchunda')

class sedan(Car):
    comport = 100

    def __init__(self, _comport=100):
        super().__init__()
        self.comport = _comport

    def run(self):#overriding
        print('sedan dalinda')

    def __add__(self, other):#overloading(other도 받아준다.)
        temp = sedan()
        temp.comport = self.comport+other.comport
        return temp#값변경을 막기위해 새로운 object를 넘겨줌.


c1 = Car()
c2 = Car(8,8)
s1 = sedan()#tire, man도 받고싶으면 위에서 받아 넘겨주면 됨.
s2 = sedan()

s3=s1+s2

print(c1.tire, c1.man)
print(c2.tire, c2.man)
print(s1.tire, s1.man, s1.comport)
print(s3.comport)

c1.run()
s1.run()#overriding
c2.stop()

del c1
del c2
