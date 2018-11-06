import pr2

class point3(pr2.point3):

    def compare(self,other):
        temp = point3()
        temp.x = max(self.x, other.x)
        temp.y = max(self.y, other.y)
        temp.z = max(self.z, other.z)
        return temp
    
if(__name__=='__main__'):
    p1 = point3(int(input()),int(input()),int(input()))
    p2 = point3(int(input()),int(input()),int(input()))

    p3 = p1.compare(p2)

    print(p3.x, p3.y, p3.z)
