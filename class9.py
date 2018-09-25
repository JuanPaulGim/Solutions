from sys import stdin 
from collections import deque
INF = float('inf')
def to_num(t):
	return t[0]*1000+t[1]*100+t[2]*10+t[3]

def next_states(t):
	ans = list()
	for i in range(4):
		tmp1, tmp2 = list(), list()
		for j in range(4):
			if j == i:
				tmp1.append((t[i]+1) if t[i]<9 else 0)
				tmp2.append((t[i]-1) if t[i]>0 else 9)
			else:
				tmp1.append(t[j])
				tmp2.append(t[j])
		ans.append(tuple(tmp1))
		ans.append(tuple(tmp2))
	return ans

def bfs(source, target):
	visited = [0]*10000
	dist = [INF for _ in range(10000)]
	queue = deque(); queue.append((source,0))
	visited[to_num(source)] = 1
	while dist[to_num(target)]== INF and len(queue) != 0:
		u,d = queue.popleft()
		dist[to_num(u)] = d
		for v in next_states(u):
			if visited[to_num(v)] == 0:
				queue.append((v,d+1)); visited[to_num(v)] = 1
		visited[to_num(u)] = 2
	return dist[to_num(target)]