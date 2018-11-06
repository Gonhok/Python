class point:
    x=0
    y=0

    def __init__(self,_x=0,_y=0):
        self.x = _x
        self.y = _y
    
    def __add__(self,other):
        temp=point()
        temp.x = self.x+other.x
        temp.y = self.y+other.y
        return temp

if(__name__=='__main__'):

    p1 = point(int(input()),int(input()))
    p2 = point(int(input()),int(input()))

    p3 = p1+p2

    print(p3.x,p3.y)
