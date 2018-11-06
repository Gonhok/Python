x=1

def f1():
    global x
    x=99
    print(x)

for _ in range(3):
    y=1
    print(x)

f1()

print(x)
