def myMaxMin(L,start,end):
    if end-start==1:
        return (max(L[start],L[end]),min(L[start],L[end]))
    else:
        max1,min1=myMaxMin(L,start,(start+end)//2)
        max2,min2=myMaxMin(L,(start+end)//2+1,end)
        return  max((max1,max2)),min(min1,min2)


def maxMin(L):
    assert (type(L) == type([]) and len(L) > 0)
    maxV, minV = myMaxMin(L, 0, len(L) - 1)
    print(maxV, minV)
    return maxV, minV


L = [1, 3, 5, 6, 7, 8, 5, 7, 8, -9]
maxMin(L)
