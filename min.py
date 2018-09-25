from collections import deque
Infinite = float('inf')

def BFS(G,l,raiz):
 q = deque()
 q.append(raiz)
 while q:
  u = q.popleft()
  for v in G[u]:
   if M[v] == Infinite:
   	M[v] = raiz
   	q.append(v)

def mini(G,L,n):
 global M
 M = [Infinite for i in range(n)]
 for (v,l) in L:
  if M[v] == Infinite:
   M[v] = v
   BFS(G,l,v)
 print(M)

def main():
 G = [[1,2],[3,5],[4],[],[0],[]]
 R = [[] for i in range(len(G))] 
 L = [(0,6),(1,5),(2,2),(3,3),(4,1),(5,4)]
 L.sort(key=lambda tup:tup[1])
 for u in range(len(G)):
  for v in G[u]:
   R[v].append(u)
 mini(R,L,len(R))
main()