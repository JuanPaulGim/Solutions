import random
def f(l):
    cnt = 0
    for lo in range(len(l)):
        i_min = lo
        for i in range(lo+1, len(l)):
            if l[i] < l[i_min]:
                i_min = i

        cnt += i_min - lo
        x = l[i_min]
        l[lo+1:i_min+1] = l[lo:i_min]
        l[lo] = x
    
    return cnt


def g(l,lo,hi):
    #Minima cantidad de flips para ordenar l[lo:hi]
    
    #Conquistar
    if hi-lo <= 1:
        return 0
    #Dividir
    mid = (lo+hi)//2
    cnt = g(l,lo,mid)
    cnt += g(l,mid,hi)
    #Combinar
    aux = []
    i = lo
    j = mid
    while i<mid and j<hi:
        if l[i] <= l[j]:
            aux.append(l[i])
            i+=1
        else:
            aux.append(l[j])
            j+=1
            cnt+= mid-i
    while i < mid:
        aux.append(l[i])
        i+=1
    while j < hi:
        aux.append(l[j])
        j+=1
    l[lo:hi] = aux
    return cnt


#Busqueda Binaria
def binary_search(l,lo,hi,x):
    if hi-lo == 0:
        return -1
    elif hi-lo == 1:
        if l[lo] == x: return lo
        else: return 0
    mid = (lo+hi)//2
    if x<l[mid]:
        return binary_search(l,lo,mid,x)
    elif l[mid] < x:
        return binary_search(l,mid,hi,x)
    else:
        i = binary_search(l,lo,mid,x)
        if i == -1: return mid
        else: return i

#Subarreglo de suma máxima

def sub_mid(a,lo,mid,hi):
    i = mid-1
    best_left = acum = a[i]
    for i in range(mid-1,lo-1,-1):
        acum+=a[i]    
        best_left = max(best_left,acum)        

    best_right = acum = 0
    for i in range(mid,hi):
        acum+=a[i]
        best_rigth = max(best_right, acum)
    return best_left + best_right

def sub_arr_sum(a,lo,hi):
    if lo==hi:
        return 0
    elif lo+1==hi:
        return max(0,a[lo])
    
    mid = (lo+hi)>>1 #Corrimiento binario
    ans_left = sub_arr_sum(a,lo,mid)
    ans_right = sub_arr_sum(a,lo,mid)
    ans_mid = sub_mid(a,lo,mid,hi)

    return max(ans_left,ans_right,ans_mid)

a = [10,1,-11,5,5,1]
print(a)
print(sub_arr_sum(a,0,len(a)))






















