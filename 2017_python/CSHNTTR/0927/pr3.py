import math

z= list(input())

per = {'a':7,'b':9,'c':11,'d':13,'e':3,'f':20,'g':5,'h':30,'i':2,'j':5}

sum=z.count('a')*per['a']\
    +z.count('b')*per['b']\
    +z.count('c')*per['c']\
    +z.count('d')*per['d']\
    +z.count('e')*per['e']\
    +z.count('f')*per['f']\
    +z.count('g')*per['g']\
    +z.count('h')*per['h']\
    +z.count('i')*per['i']\
    +z.count('j')*per['j']\

count= z.count('a')\
       +z.count('b')\
       +z.count('c')\
       +z.count('d')\
       +z.count('e')\
       +z.count('f')\
       +z.count('g')\
       +z.count('h')\
       +z.count('i')\
       +z.count('j')\
    
print(math.ceil(sum/count))
