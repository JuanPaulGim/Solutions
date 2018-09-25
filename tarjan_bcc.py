def dfs_tarjan(u):
 low[u] = depth[u]
 for v in G[u]:
  if depth[v] == -1:
   depth[v] = depth[u]+1
   papa[v] = u
   dfs_tarjan(v)
   low[u] = min(low[u],low[v])
  elif  v == papa[u]:
   pass # u is in G[v] and depth[v]<depth[u]
  else:	
   low[u] = min(low[u],depth[v])
 return 

def main():
 global low, depth, papa, comps
 n = len(G)
 low = [-1 for i in range(n)]
 depth = [-1 for i in range(n)]
 papa = [-1 for i in range(n)]
 for u in range(n):
  if depth[u] == -1:
   depth[u] = 0
   dfs_tarjan(u)
 print(low)
 print(depth)

G = [[3],
     [0,2],
     [4],
     [5],
     [1],
     []
]
main()