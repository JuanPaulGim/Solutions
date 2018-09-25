import sys
sys.setrecursionlimit(10**6)
#representacion arbol bin
#Listas
Arb = [3,[2,10,7],[4,None,9]]
Arb = [4,[5,[3,4,None],3],[4,[2,7,None],[9,13,None]]]

#representacion arbol bin
#Clases
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
A = BinTree(3,BinTree(2,BinTree(10),BinTree(7)),BinTree(4,BinTree(3),BinTree(9)))

#Def ArbBin := num | None | (ArbBin) num (ArbBin)
def print_tree1(x):
	if type(x) != list and x != None:
		print(x,end='')
	elif x == None:
		print("",end='')
	else:
		print('(',end='')
		print_tree1(x[1])
		print(')',end='')
		print(x[0],end='')
		print('(',end='')
		print_tree1(x[2])
		print(')',end='')
	return

#operaciones principales
#Indexando desde 1
	#papa(i) = i//2
	#left(i) = 2i
	#right(i) = 2i+1
Arb = ['?',3,2,4,10,7,4,9] #En orden de BFS
def print_tree2(x,r):
	if 2*r < len(x):
		print('(',end='')
		print_tree2(x,2*r)
		print(')',end='')
	print(x[r],end='')
	if 2*r+1 <len(x):
		print('(',end='')
		print_tree2(x,2*r+1)
		print(')',end='')
