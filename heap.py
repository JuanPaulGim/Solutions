import random
#Minmal Heaps
class miheap(object):
	"""Minimal Heap implementation"""
	def __init__(self):
		self.__heap = list()
	def __len__(self):
		return len(self.__heap)
	def __str__(self):
		return str(self.__heap)
	def __parent(self,i):
		assert i > 0
		return (i-1)>>1
	def __left(self,i):
		return 1+(i<<1)
	def __right(self,i):
		return (1+i)<<1
	def insert(self,x):
		self.__heap.append(x)
		if len(self) > 1:
			self.__heapify_up(len(self)-1)
	def __heapify_up(self,i):
		if i != 0:
			ip = self.__parent(i)
			if self.__heap[ip] > self.__heap[i]:
				self.__heap[ip],self.__heap[i] = self.__heap[i],self.__heap[ip]
				self.__heapify_up(ip)
	def get_min(self):
		assert len(self) != 0
		return self.__heap[0]
	def remove_min(self):
		assert len(self) != 0
		self.__heap[0] = self.__heap[-1]
		self.__heap.pop()
		if len(self)>1:
			self.__heapify_down(0)
	def __heapify_down(self,i):
		il,ir = self.__left(i),self.__right(i)
		if il < len(self):
			best = i
			if self.__heap[il]<self.__heap[i]: best = il
			if ir < len(self) and self.__heap[ir] < self.__heap[il]: best = ir
			if best != i:
				self.__heap[i],self.__heap[best] = self.__heap[best],self.__heap[i] 
				self.__heapify_down(best)

h = miheap()
for i in range(10):
	h.insert(random.randrange(-1000,1000))
print(h)
