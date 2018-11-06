import math
import pr4

class point3(pr4.point3):
    def distance(self,other):
        return math.sqrt(pow(self.x-other.x,2)+pow(self.y-other.y,2)\
                         +pow(self.z-other.z,2))
    

if(__name__=='__main__'):

    p1 = point3(int(input()),int(input()),int(input()))
    p2 = point3(int(input()),int(input()),int(input()))

    print('%.2f'%p1.distance(p2))
