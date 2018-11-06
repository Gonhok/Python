import pr1

class point3(pr1.point):
    z=0

    def __init__(self,_x=0,_y=0,_z=0):
        super(point3, self).__init__(_x,_y)
        self.z = _z

    def adder(self,other):
        print(self.x+other.x, self.y+other.y, self.z+other.z)


if(__name__=='__main__'):

    p1 = point3(int(input()),int(input()),int(input()))
    p2 = point3(int(input()),int(input()),int(input()))

    p1.adder(p2)
