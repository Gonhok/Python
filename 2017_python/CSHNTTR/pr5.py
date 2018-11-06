x = int(input())

bus = x//23

teacher = bus + x%23//3 +x%23%3//2 + x%23%3%2//1
#

print(bus,teacher)
