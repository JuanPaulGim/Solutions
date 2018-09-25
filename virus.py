import sys
from sys import stdin
from collections import deque

def solve(src,tgt,ti,tf,n):
 visited = [False for i in range(n)]	
 visited[src] = True
 for u,v,t in G:
  if(visited[u] == True and visited[v] == False):
   if ti<=t<=tf:
    visited[v] = True
  elif(visited[u] == False and visited[v] == True):
   if ti<=t<=tf:
    visited[u] = True
 if visited[tgt]:
  return 1    
 return 0 
def main():
 global G,visited	
 nm = sys.stdin.readline().split(" ")
 n,m = int(nm[0]),int(nm[1])
 while(n!=0 or m!=0):
  data = sys.stdin.readline().split(" ")
  src,tgt,ti,tf = int(data[0]),int(data[1]),int(data[2]),int(data[3])
  G=[]
  for i in range(m):
   trip = sys.stdin.readline().split(" ")
   u,v,t = int(trip[0]),int(trip[1]),int(trip[2])
   G.append((u,v,t))
  print(solve(src,tgt,ti,tf,n))
  nm = sys.stdin.readline().split(" ")
  n,m = int(nm[0]),int(nm[1])


main()