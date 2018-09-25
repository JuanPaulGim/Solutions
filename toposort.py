
def topo_sort(G):
 ans = []
 indeg = [0 for _ in range(len(G))]
 for u in range(len(G)):
  for v in G[u]:
   indeg[v]+=1
 pending = list()
 for u in range(len(G)):
  if indeg[u] == 0:
   pending.append(u)
 while len(pending) != 0:
  u = pending.pop()
  ans.append(u)
  for v in G[u]:
   indeg[v] -=1
   if indeg[v] == 0:
   	pending.append(v)
 return ans

G = [[],
     [4,6],
     [7],
     [4,7],
     [5],
     [],
     [],
     [5]]

print(topo_sort(G))
 	
