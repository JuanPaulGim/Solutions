import sys
sys.setrecursionlimit(100000000)
from sys import stdin


def bs(A,x,low,hi):
	cent = False
	ans = -1
	while not cent:
	 mid = (hi+low)//2
	 if A[mid] > x:
	  hi = mid
	 elif A[mid] < x:
	  low = mid
	 else:
	  cent = True
	  ans = mid
	return ans
def merge(A):
	
#

L = [2,3,4,5,6,7,8,9,10,33,44,55,66]
print(bs(L,10,0,len(L)))

alg: A->B

L[0,1,2,3,4]
A = 0, B = 4
P0 = alg siempre esta en un C [A,B]
#Inicializacion
P0 se cumple por que alg inicia A y A está en [A,B]
#Estabilidad
alg avanza maximo hasta B, luego alg siempre está en [A,B]
#Finalizacion
el resultado esta en [A,B] porque el resultado es B

