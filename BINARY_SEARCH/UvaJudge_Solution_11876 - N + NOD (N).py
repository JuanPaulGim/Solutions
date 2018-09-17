#Autor: Juan Pablo Giraldo Mosquera / 8934332
#Colaboradores: Juan Esteban Cardona, Josue Peña 
import sys
from sys import stdin

N = [0]*1100000
primos = []
booleanflags = [1]*1000000
booleanflags[6] = 0
#Divisores
def NOD(x):
	i = 0
	f = primos[i] #Factor primo
	divs = 1
	while ((f*f) <= x):
		p = 0
		while(x%f == 0):
			x = x/f
			p +=1 #Potencias de cada primo que caben en X
		divs = divs*(p+1)
		i+=1
		f = primos[i]
	if(x != 1):
		divs= divs*2
	return divs
	
#Calculo de los primeros n primos
def criba_eratostenes(n):
   booleanflags[0] = 0
   booleanflags[1] = 0
   i = 2
   while(i < n+1):
   	if booleanflags[i] == 1:
   		j = i*i
   		while(j <= n+1):
   			booleanflags[j] = 0
   			j+=i
   		primos.append(i)
   	i+=1

def fill():
	i = 1
	Ni = 1
	N[Ni] = Ni
	while(i < 65000):
		Ni += NOD(Ni)
		N[Ni] = i+1
		i+=1


def solve(A, B):
	while N[A] == 0:
		A+=1
	while N[B] == 0:
		B-=1
	return N[B] - N[A] +1
def main():
  criba_eratostenes(1000)
  fill()
  tcnt = int(stdin.readline())
  for tc in range(1, tcnt+1):
    A,B = map(int, stdin.readline().split())
    print('Case {0}: {1}'.format(tc, solve(A, B)))

main()