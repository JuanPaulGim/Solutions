def gabow_scc(G):
 global marked,idi,preorder,pre,count,stack1,stack2
 marked = [0 for i in range(len(G))]
 idi = [-1 for i in range(len(G))]
 preorder = [0 for i in range(len(G))]
 count = 0
 pre = 0
 stack1,stack2 = [],[]
 for v in range(len(G)):
  if marked[v] == 0:
   DFS(v)
 print_scc()
 print(preorder)
def DFS(v):
 global marked,idi,preorder,pre,count,stack1,stack2
 marked[v] = 1
 preorder[v] = pre
 pre+=1
 stack1.append(v);stack2.append(v)
 for w in G[v]:
  if marked[w] == 0:
   DFS(w)
  elif idi[w] == -1:
   while preorder[stack2[len(stack2)-1]] > preorder[w]:
   	stack2.pop()
 if stack2[len(stack2)-1] == v:
  stack2.pop()
  w = stack1.pop()
  idi[w] = count
  while w != v:
   w = stack1.pop()
   idi[w] = count
  count+=1
def print_scc():
 global marked,idi,preorder,pre,count,stack1,stack2
 print(count)
 for i in range(count):
  comp = []
  for v in range(len(G)):
   if idi[v] == i:
    comp.append(v)
  print(comp)	


G = [[1],
	 [2],
	 [3],
	 [0,4],
	 [5],
	 [6],
	 [7],
	 [8],
	 [9],
	 [10],
	 []
	]

gabow_scc(G)



