# -*- encoding: utf-8 -*-

def isPrime(num):
	return len(filter(lambda x: num%x==0, [n for n in range(1,num+1)])) == 2

import math
def fastPrime(n):
	if n%2 == 0 and n > 2:
        	return False
	return all(n%i for i in range(3, int(math.sqrt(n))+1, 2)) 

#print(fastPrime(2))
print(fastPrime(pow(2,128)-1))

#print(filter(fastPrime, [n for n in range(1, 10000)]))
