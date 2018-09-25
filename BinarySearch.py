import random

def binarysearch(A,x):
	""" A is ordered (ascending) and contains numbers; x is a number.
	    This function checks if x is an element of A"""
	N = len(A)
	assert N>=1
	low,hi = 0,N
	ops = 0
	while low+1 != hi:
		mid = low+((hi-low)>>1)
		if x<A[mid]:
			hi=mid
		else:
			low = mid
		ops+=1	

	print(ops)
	return A[low] == x

a = [random.randrange(0,10000000) for i in range(1000)]
print(binarysearch(a,6))