from sys import stdin


def solve(target): 
  ans = ""
  n1,d1,n2,d2 = 0,1,1,0
  while(n1+n2 != target[0] and d1+d2 != target[1]):
  		if(target[0]*(d1+d2) > target[1]*(n1+n2)):
  			ans+="R"
  			n1 = n1+n2
  			d1 = d1+d2
  		elif (target[0]*(d1+d2) < target[1]*(n1+n2)):
  			ans+="L"
  			n2 = n1+n2
  			d2 = d1+d2
  return ans

def main():
  target = [int(x) for x in stdin.readline().strip().split()]
  while target[0]!=1 or target[1]!=1:
    print(solve(target))
    target = [int(x) for x in stdin.readline().strip().split()]

main()
