def dec_mitad(arr,low,hi,mid):
 i,j = mid, mid
 izq = 0
 der = 0
 nxt = -1000
 ok = True
 while (i >= low and ok):
  if (arr[i] > nxt):
   izq += 1
   nxt = arr[i]
   ok = True
  i-=1
 while j+1 < hi:
  if (arr[j] > arr[j+1]):
   der+=1 
  else:
   break
  j+=1
 return der + izq

def decreciente(arr,low,hi):
 if(hi-low == 1):
  return 1
 elif(hi-low < 1):
  return 0
 mid = (hi+low)//2
 izq = decreciente(arr,low,mid)
 der = decreciente(arr,mid,hi)
 mitad = dec_mitad(arr,low,hi,mid)
 return max(izq,der,mitad)

L = [20,19,18,17,7,4,3,2,1,10,11,12,10,5,3,2,1]
print(decreciente(L,0,len(L)))
L = [4,3,2,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(decreciente(L,0,len(L)))
L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,6,5,4,3,2,1]
print(decreciente(L,0,len(L)))