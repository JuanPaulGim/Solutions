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

def find_points(Ly,A):
	q = deque()
	ans = 0
	q.append(A)
	while len(q) != 0:
		point = q.popleft()
		if point != None:
			x,y = point.num
			if y != None and point.lvl%2 == 1 and y > Ly:
				ans+=1
				q.append(point.l)
				q.append(point.r)
			elif y != None and point.lvl%2 == 1 and y <= Ly:
				q.append(point.l)
				q.append(point.r)
			elif y != None and point.lvl%2 == 0 and y >= Ly:
				if y > Ly:
					ans+=point.lenr+1
				else:
					ans+=point.lenr
				q.append(point.l)
			elif y != None and point.lvl%2 == 0 and y < Ly:
				q.append(point.r)
	return ans
Kd_tree1 = KdTree((4,1),KdTree((3,5),KdTree((1.5,4.5),KdTree((0.5,1.5),None,None,0,0,4),KdTree((2.5,3.5),None,None,0,0,4),1,1,3),KdTree((2,6),KdTree((1,7),None,None,0,0,4),KdTree((3.5,8.5),None,None,0,0,4),1,1,3),3,3,2),
	KdTree((7,4),KdTree((6,3),KdTree((5,2),None,None,0,0,4),KdTree((7.5,2.5),None,None,0,0,4),1,1,3),KdTree((5.5,6.5),KdTree((4.5,7.5),None,None,0,0,4),KdTree((6.5,5.5),None,None,0,0,4),1,1,3),3,3,2),7,7,1)
Kd_tree2 = KdTree((2,1),KdTree((1,3),None,None,0,0,2),KdTree((3,2),None,None,0,0,2),1,1,1)
Kd_tree3 = KdTree((7,6))
#print(Kd_tree)
print(find_points(3.5,Kd_tree1))
print(find_points(0.5,Kd_tree2))