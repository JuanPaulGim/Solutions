import sys
from sys import stdin

def check_nat(N):
 if N[0] != 0:
  return 0
 for i in range(len(N)-1):
  if N[i]+1 != N[i+1]:
  	return N[i]+1
 return -1

L = sys.stdin.readline()
L = L.split(" ")
L = [int(L[i]) for i in range(len(L))]
print(check_nat(L))