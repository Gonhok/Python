x=set(input())
y=set(input())

z=x|y
z= z-(x&y)

z1 = list(z)

z1.sort()

print(z1)
