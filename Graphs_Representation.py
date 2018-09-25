from sys import stdin

G = [[1,2,3], # 0
	 [0,2], # 1
	 [1,0], # 2
	 [0], # 3
	 [5,7], # 4
	 [4,7], # 5
	 [],  # 6
	 [4,5], ] 
# de lista a matriz
n = 8
M = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
	for j in G[i]:
		M[i][j] = 1

# de matriz a lista
n = len(M)
G = [[] for i in range(n)]
for i in range(n):
	for j in range(n):
		if M[i][j] == 1:
			G[i].append(j)

# de matriz a lista de arcos
n = len(M)
E = []
for i in range(n):
	for j in range(n):
		if M[i][j] == 1:
			E.append((i,j))
# de lista de arcos a lista de adyacencia 
G = [[] for i in range(n)]
for (i,j) in E:
	G[i].append(j)

# De dirigido a no -dirigido
G = [[1,2], # 0
	 [], # 1
	 [1], # 2
	 [0], # 3
	 [4,7], # 4
	 [], # 5
	 [4],   # 6
	 ]
n  = 7
G2 = [[] for i in range(n)]
for i in range(n):
	for j in G[i]:
		G2[i].append(j)
		G2[j].append(i)

G2 = [list(set(l)) for l in G2]
print(G2)