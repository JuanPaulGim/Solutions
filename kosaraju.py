from collections import deque
def dfs1(u):
 vis[u] = 1
 for v in R[u]:
  if vis[v] == 0:
   dfs1(v)
 d.appendleft(u)
 return
def dfs2(u):
 vis[u] = 1
 scc[u] = scc_cnt
 for v in G[u]:
  if vis[v] == 0:
   dfs2(v)
 return

def main():
 global R, vis, d, scc, scc_cnt
 n = len(G)
 R = [[] for i in range(n)]
 for u in range(n):
  for v in G[u]:
   R[v].append(u)
 d = deque()
 vis = [0 for i in range(n)]
 for u in range(n):
  if vis[u] == 0:
   dfs1(u)
 scc = [-1 for i in range(n)]
 scc_cnt = 0
 vis = [0 for i in range(n)]
 for u in d:
  if vis[u] == 0:
   dfs2(u)
   scc_cnt += 1
 print(d)
 for i in range(n):
  print(i,scc[i],R[i])
 return

# Strongly conected components
# [9]
# [1,2,4]
# [3,5]
# [6]
# [7,8]
# [0]

G = [
	[1],
	[3],
	[1],
	[2]
]
main()
