def BS(arr,x,L=0,R=0):
    if R>=L:
        mid=L+(R-L)//2
        if R==0:
            R=len(arr)-1
        if x>R and x<L:
            print('Not present')
            return
        if arr[mid]==x:
            print(mid)
            return
        elif arr[mid]>x:
            BS(arr,x,L,mid-1)
        elif arr[mid]<x:
            BS(arr,x,mid+1,R)
        else:
            print('Not present')
    else:
        print('Not present')

BS([1,2,3,4],2.5)

