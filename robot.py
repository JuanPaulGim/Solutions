#Problema: 10116 - Robot Motion
#Autor: Juan Pablo Giraldo Mosquera
#Fecha: 25/08/2018
#Hora: 11:31 AM
import sys
from sys import stdin

def main():
 data_set = sys.stdin.readline(); data_set = data_set.strip(" ").split(" ")
 data_set = [int(i) for i in data_set]
 R = data_set[0]
 C = data_set[1]
 I = data_set[2]
 while R != 0 and C != 0 and I != 0: 
  mat = []
  visited = [[False for i in range(C)] for i in range(R)]
  steps = [[0 for i in range(C)] for i in range(R)]
  for i in range(R):
   row = sys.stdin.readline()
   mat.append(row)
  stack = []
  x,y = 0,I-1
  #l1,l2 = Posicion del inicio del ciclo
  l1,l2 = -1,-1
  stack.append(mat[x][y])
  if y < len(visited[x]):
   visited[x][y] = True
   steps[x][y] = 1
  #DFS para contar los pasos que da el robot y verificar si existe un ciclo
  while stack:
   ins = stack.pop()
   visited[x][y] = True
   if ins == "W":
    if y-1 >= 0 and visited[x][y-1] != True:
     stack.append(mat[x][y-1])
     steps[x][y-1] = 1 + steps[x][y]
     y-=1
    elif 0<=y-1<C and visited[x][y-1] == True:
     l1,l2 = x,y-1
   elif ins == "E":
    if y+1 < C and visited[x][y+1] != True:
     stack.append(mat[x][y+1])
     steps[x][y+1] = 1 + steps[x][y]
     y+=1
    elif 0<=y+1<C and visited[x][y+1] == True:
     l1,l2 = x,y+1
   elif ins == "S":
    if x+1 < R and visited[x+1][y] != True:
     stack.append(mat[x+1][y])
     steps[x+1][y] = 1 + steps[x][y]
     x+=1
    elif 0<=x+1<R and visited[x+1][y] == True:
     l1,l2 = x+1,y
   elif ins == "N":
    if x-1 >= 0 and visited[x-1][y] != True:
     stack.append(mat[x-1][y])
     steps[x-1][y] = 1 + steps[x][y]
     x-=1
    elif 0<=x-1<R and visited[x-1][y] == True:
     l1,l2 = x-1,y
  #Calculo de los pasos que componen el ciclo y los pasos antes de llegar al mismo   
  if l1 != -1:
   if mat[l1][l2] == "N":
    if 0<=l1+1<R and l1+1 != x and visited[l1+1][l2] == True and steps[l1][l2] > steps[l1+1][l2]:
     print(steps[l1+1][l2],"step(s) before a loop of",steps[x][y]-steps[l1+1][l2],"step(s)")
    elif 0<=l2+1<C and l2+1 != y and visited[l1][l2+1] == True and steps[l1][l2] > steps[l1][l2+1]:
     print(steps[l1][l2+1],"step(s) before a loop of",steps[x][y]-steps[l1][l2+1],"step(s)")
    elif 0<=l2-1<C and l2-1 != y and visited[l1][l2-1] == True and steps[l1][l2] > steps[l1][l2-1]:
     print(steps[l1][l2-1],"step(s) before a loop of",steps[x][y]-steps[l1][l2-1],"step(s)")
    else:
   	 print("0 step(s) before a loop of",steps[x][y],"step(s)")
   elif mat[l1][l2] == "S":
    if 0<=l1-1<R and l1-1 != x and visited[l1-1][l2] == True and steps[l1][l2] > steps[l1-1][l2]:
     print(steps[l1-1][l2],"step(s) before a loop of",steps[x][y]-steps[l1-1][l2],"step(s)")
    elif 0<=l2+1<C and l2+1 != y and visited[l1][l2+1] == True and steps[l1][l2] > steps[l1][l2+1]:
     print(steps[l1][l2+1],"step(s) before a loop of",steps[x][y]-steps[l1][l2+1],"step(s)")
    elif 0<=l2-1<C and l2-1 != y and visited[l1][l2-1] == True and steps[l1][l2] > steps[l1][l2-1]:
     print(steps[l1][l2-1],"step(s) before a loop of",steps[x][y]-steps[l1][l2-1],"step(s)")
    else:
   	 print("0 step(s) before a loop of",steps[x][y],"step(s)")
   elif mat[l1][l2] == "E":
    if 0<=l1+1<R and l1+1 != x and visited[l1+1][l2] == True and steps[l1][l2] > steps[l1+1][l2]:
     print(steps[l1+1][l2],"step(s) before a loop of",steps[x][y]-steps[l1+1][l2],"step(s)")
    elif 0<=l1-1<R and l1-1 != x and visited[l1-1][l2] == True and steps[l1][l2] > steps[l1-1][l2]:
     print(steps[l1-1][l2],"step(s) before a loop of",steps[x][y]-steps[l1-1][l2],"step(s)")
    elif 0<=l2-1<C and l2-1 != y and visited[l1][l2-1] == True and steps[l1][l2] > steps[l1][l2-1]:
     print(steps[l1][l2-1],"step(s) before a loop of",steps[x][y]-steps[l1][l2-1],"step(s)")
    else:
   	 print("0 step(s) before a loop of",steps[x][y],"step(s)")
   elif mat[l1][l2] == "W":
    if 0<=l1+1<R and l1+1 != x and visited[l1+1][l2] == True and steps[l1][l2] > steps[l1+1][l2]:
     print(steps[l1+1][l2],"step(s) before a loop of",steps[x][y]-steps[l1+1][l2],"step(s)")
    elif 0<=l1-1<R and l1-1 != x and visited[l1-1][l2] == True and steps[l1][l2] > steps[l1-1][l2]:
     print(steps[l1-1][l2],"step(s) before a loop of",steps[x][y]-steps[l1-1][l2],"step(s)")
    elif 0<=l2+1<C and l2+1 != y and visited[l1][l2+1] == True and steps[l1][l2] > steps[l1][l2+1]:
     print(steps[l1][l2+1],"step(s) before a loop of",steps[x][y]-steps[l1][l2+1],"step(s)")
    else:
   	 print("0 step(s) before a loop of",steps[x][y],"step(s)")
  else:
   print(steps[x][y],"step(s) to exit")
  data_set = sys.stdin.readline(); data_set = data_set.strip(" ").split(" ")
  data_set = [int(i) for i in data_set]
  R = data_set[0]
  C = data_set[1]
  I = data_set[2]
main()