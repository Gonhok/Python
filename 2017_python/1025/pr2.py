def isPrime(x):
    if x ==1 or x==2:
        return 1
    
    for i in range(2,x-1):
        if x%i==0:
            return 0
    return 1

#	for i in range(2, int(x**0.5)+1):
#		if	(fx%i==0):
#			return 0
#	return 1
	
	
if __name__== '__main__':
    a = int(input())
    print(isPrime(a))
	
l1 = [i for i in range(1,100) if (isPrime(i))]
print(l1)
