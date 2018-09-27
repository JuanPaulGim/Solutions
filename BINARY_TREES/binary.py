import sys
from sys import stdin
sys.setrecursionlimit(10**6)

class BinTree:
	def __init__(self,num,left=None,right=None):
		self.num = num
		self.l = left
		self.r = right
		return
	def __str__(self):
		str_l = str(self.l) if self.l != None else ''
		str_r = str(self.r) if self.r != None else ''
		s='{} ({}) ({})'.format(self.num,str_l,str_r) 
		return s

def merge_sort(low, hi):
	if hi-low <= 1:
		return
	mid = (low+hi)//2
	merge_sort(low,mid)
	merge_sort(mid,hi)
	aux = []
	i = low
	j = mid
	while i < mid and j < hi:
	  	if inorder[i] <= inorder[j]:
	  		aux.append(inorder[i])
	  		i+=1
	  	else:
	  		aux.append(inorder[j])
	  		j+=1
	while i < mid:
	  	aux.append(inorder[i])
	  	i+=1
	while j < hi:
	  	aux.append(inorder[j])
	  	j+=1
	inorder[low:hi] = aux

def build_tree(pre,ino):
	if len(pre) > 1:
		ind = ino.index(pre[0])
		return BinTree(pre[0],build_tree(pre[1:ind+1],ino[:ind+1]),build_tree(pre[ind+1:],ino[ind+1:]))
	elif len(pre) == 1:
		return BinTree(pre[0])

def post(t):
	if t.l != None:
		postorder.append(post(t.l))
	if t.r != None:
		postorder.append(post(t.r))
	return t.num

def main():
	global inorder,postorder
	node = stdin.readline()
	preorder = []
	inorder = []
	postorder = []
	while node:
		node = int(node)
		preorder.append(node)
		inorder.append(node)
		node = stdin.readline()
	merge_sort(0,len(inorder))
	tree = build_tree(preorder,inorder)
	post(tree)
	postorder.append(preorder[0])
	for i in range(len(postorder)):
		print(postorder[i])
main()