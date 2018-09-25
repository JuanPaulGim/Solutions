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

def preorder(tree):
	if(tree.l != None):
		if(tree.num not in lista):
			lista.append(tree.num)
		new = preorder(tree.l)
		if new not in lista:
			lista.append(new)

	if(tree.r != None):
		if(tree.num not in lista):
			lista.append(tree.num)
		new = preorder(tree.r)
		if new not in lista:
			lista.append(new)
	return tree.num

def inorder(tree):
	if tree.l != None:
		new = inorder(tree.l)
		if new not in lista:
			lista.append(new)
	if tree.num not in lista:
		lista.append(tree.num)
	if tree.r != None:
		new = inorder(tree.r)
		if new not in lista:
			lista.append(new)
	return tree.num
def postorder(tree):
	pass

def main():
	global lista
	lista = []
	Arbol = BinTree(4,BinTree(3,BinTree(1),BinTree(7)),BinTree(6,BinTree(2),BinTree(5)))
	inorder(Arbol)
	print(lista)

main()