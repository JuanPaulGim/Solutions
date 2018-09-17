import sys
from sys import stdin

def solve(G,m):
 ans = []
 indeg = [0 for _ in range(len(G))]
 components = [0 for _ in range(len(G))]
 comp = 1
 last = 1
 for u in range(len(G)):
  for v in G[u]:
   indeg[v]+=1
 pending = list()
 for u in range(len(G)):
  if indeg[u] == 0:
   pending.append(u)
 while len(pending) != 0:
  u = pending.pop()
  if components[u] == 0:
   components[u] = comp
  ans.append(u)
  flag = True
  for v in G[u]:
   flag = False
   indeg[v] -=1
   if indeg[v] == 0:
    pending.append(v)
    components[v] = components[u]
  if flag:
   last+=1
  if flag and components[u] == comp:
   comp+=1
 if comp == last and len(ans) == len(G):
  return 1
 else:
  print(comp)
  return 0

def main():
 line = sys.stdin.readline().split(" ")
 n,m = int(line[0]),int(line[1])
 while n != 0 or m != 0:
  G = [[] for i in range(n)]
  for i in range(m):
   line = sys.stdin.readline().split(" ")
   a,b = int(line[0]),int(line[1])
   G[a].append(b)
  print(solve(G,m))
  line = sys.stdin.readline().split(" ")
  n,m = int(line[0]),int(line[1])
main()