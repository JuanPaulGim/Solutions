import sys
sys.setrecursionlimit(1000000)
def f(Arb):
 if type(Arb) == int:
  return Arb
 elif Arb[0] == '+':
  ans = 0
  for i in range(1,len(Arb)):
   value = f(Arb[i])
   ans += value
  return ans
 elif Arb[0] == '-':
  ans = 0
  for i in range(1,len(Arb)):
   value = f(Arb[i])
   ans-=value
  return ans
 elif Arb[0] == '*':
  ans = 1
  for i in range(1,len(Arb)):
   value = f(Arb[i])
   ans*= value
  return ans
 elif Arb[0] == '/':
  ans = 1
  for i in range(1,len(Arb)):
   value = f(Arb[i])
   ans/=value
  return ans
 
 	
def main():
 Arb = ['*',['+',['*',['+',7,['*',2,4]],1],['*',-1,['+',1,0,2]]],['+',3,0]]
 print(f(Arb))
main()
