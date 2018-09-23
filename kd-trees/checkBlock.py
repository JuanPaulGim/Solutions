from collections import deque

class KdTree:
	def __init__(self,num,left=None,right=None,lenleft=0,lenright=0,level=0):
		self.num = num
		self.l = left
		self.r = right
		self.lenl = lenleft
		self.lenr = lenright
		self.lvl = level
		return
	def __str__(self):
		str_l = "("+str(self.l)+")" if self.l != None else ''
		str_r = "("+str(self.r)+")" if self.r != None else ''
		s='{} {} {}'.format(self.num,str_l,str_r) 
		return s.strip()

#Asumir que Ly1 < Ly2 y Lx1 < Lx2
def find_points(Ly1,Ly2,Lx1,Lx2,A):
	q = deque()
	ans = 0
	q.append(A)
	while len(q) != 0:
		point = q.popleft()
		if point != None:
			x,y = point.num
			if point.lvl % 2 == 1: #Caso impar, solo descarto basado en X
				if Lx1 >= x: #Descartar izquierdo si Lx1 >= x porque significa que point hace parte de Lx1 o esta antes de ella
					q.append(point.r)
				elif Lx2 <= x: #Descartar derecho si Lx2 <= x porque significa que point hace parte de Lx2 o esta despues de ella
					q.append(point.l)
				elif Ly1 < y < Ly2: #Si se llega a evaluar este caso quiere decir que no puedo descartar y verifico si el y esta en el rango
					ans+=1
					points.append(point.num)
					q.append(point.l)
					q.append(point.r)
				elif y <= Ly1 or y >= Ly2: #Si y no esta en el rango no cuento ese punto y sigo con ambos subarboles
					q.append(point.l)
					q.append(point.r)
			if point.lvl % 2 == 0: #Caso par, solo descarto basado en Y
				if Ly1 >= y: # Descartar izquierdo si Ly1 >= y por la misma razon que el caso impar
					q.append(point.r)
				elif Ly2 <= y: # Descartar derecho si Ly2 <= y por la misma razon que el caso impar
					q.append(point.l)
				elif Lx1 < x < Lx2: #Si se evalua este caso no descarte nada y verifico si el x esta en el rango	
					ans+=1
					points.append(point.num)
					q.append(point.l)
					q.append(point.r)
				elif x <= Lx1 or x >= Lx2: #Si x no esta en el rango no cuento ese punto y sigo con ambos subarboles					
					q.append(point.l)
					q.append(point.r)
	return ans

def main():
	global points
	tree = KdTree((6,1),KdTree((4,7),KdTree((5,3),KdTree((3,5),None,None,0,0,4),KdTree((5.5,6),None,None,0,0,4),1,1,3),
		KdTree((2,10),KdTree((1,8),None,None,0,0,4),KdTree((5.5,9),None,None,0,0,4),1,1,3),3,3,2),
		KdTree((10,6),KdTree((8,4),KdTree((7,5),None,None,0,0,4),KdTree((11,2),None,None,0,0,4),1,1,3),KdTree((11,11),KdTree((9,8),None,None,0,0,4),
			KdTree((12,9),None,None,0,0,4),1,1,3),3,3,2),7,7,1)
	points = []
	print(find_points(0,8,1,13,tree))
	print(points)
main()