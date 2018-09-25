#selection sort
def sel_sort(l):
    for i in range(len(l)-1):
        min = i
        j = i+1
        while j < len(l):
            if l[min] > l[j]:
                min = j
            j+=1
        tmp = l[i]
        l[i] = l[min]
        l[min] = tmp

    return l


#insertion sort

def in_sort(l):
    i = 1
    while i < len(l):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j = j - 1
        l[j+1] = key
        i+=1
        
    return l


l2 = [6,8,5,2,4,4,1,1,1,2,4,5,5]
#print (l2)
#print (in_sort(l2))


    

    



