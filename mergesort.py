def merge(l):
    if len(l)>1:
        mid=len(l)//2
        L=l[:mid]
        R=l[mid:]
        merge(L)
        merge(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]>R[j]:
                l[k]=R[j]
                j+=1
            else:
                l[k]=L[i]
                i+=1
            k+=1
        #if there is any left element in the list
        while i <len(L):
            l[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            l[k]=R[j]
            j+=1
            k+=1
    return l 
