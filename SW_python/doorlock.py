def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

list = input().split()

k = gcd(int(list[0]),int(list[1]))
print(gcd(k,int(list[2])))
