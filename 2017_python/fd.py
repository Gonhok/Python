def f1():
    print('f1')

def f2(x):
    print('x2',x)
    return x+500
    
f1()
d=f2(500)

print(d)
