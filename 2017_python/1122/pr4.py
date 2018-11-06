import pr1

class point3(pr1.point):
    z=0

    def __init__(self,_x=0,_y=0,_z=0):
        super(point3, self).__init__(_x,_y)
        self.z = _z

    def isSame(self,other):
        if(self.x-other.x==0 and self.y-other.y==0 and self.z-other.z==0):
            print('eq')
        else:
            print('not eq')


if(__name__=='__main__'):

    p1 = point3(int(input()),int(input()),int(input()))
    p2 = point3(int(input()),int(input()),int(input()))

    p1.isSame(p2)
