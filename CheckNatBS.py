import sys
from sys import stdin

def check_nat(N,low,hi):
 if N[0] != 0:
  return 0
 mid = (low+hi)//2
 ans = -1
 while hi != low+1:
  if(mid != N[mid]):
   ans = hi = mid
  else:
   low = mid
  mid = (low+hi)//2
 return ans

L = sys.stdin.readline()
L = L.split(" ")
L = [int(L[i]) for i in range(len(L))]
print(check_nat(L,0,len(L)))



 

