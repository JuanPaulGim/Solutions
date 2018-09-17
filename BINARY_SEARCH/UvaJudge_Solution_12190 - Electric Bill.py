from sys import stdin

def consume(p):
	A = [2,100,3,9900,5,990000]
	i = 0
	ans = 0
	while(i < len(A)):
		if(p//A[i] >= A[i+1]):
			ans+= A[i+1]
		elif 0<p//A[i]:
			ans+=p//A[i]
		p-=A[i]*A[i+1]
		i+=2
	if(p//7>0):
		ans+=p//7
	return ans

def cost(c):
   A = [2,100,3,9900,5,990000]
   i = 0
   ans = 0
   while(i < len(A)):
   	if((c*A[i]) >= (A[i+1]*A[i])):
   		ans+=A[i+1]*A[i]
   	elif (c*A[i]) > 0:
   		ans+=c*A[i]
   	c-=A[i+1]
   	i+=2
   if(c*7 >0):
   	ans+=c*7
   return ans

def solve(tsum, diff):
	cons = consume(tsum)
	low = 0
	hi = cons
	ans = 0
	flag = True
	while(low < hi and flag == True):
		mid = (hi+low)//2
		auxdiff = cost(cons-mid) - cost(mid)
		if(auxdiff>diff):
			low = mid
		elif(auxdiff<diff):
			hi = mid
		else:
			ans = mid
			flag = False
	return cost(ans)

def main():
  print(consume(35515))
  tsum,diff = map(int,stdin.readline().split())
  while tsum+diff!=0:
    print(solve(tsum, diff))
    tsum,diff = map(int,stdin.readline().split())

main()

