A=[[10,20,30,40],
    [15,25,35,45],
    [27,29,37,48],
    [32,33,39,50]]
x=39
l=0
r=len(A)-1
mid2=0
mid=0
while l <= r:
        l1=0
        r1=len(A[mid])-1
        mid = l + (r - l) // 2
        if x==A[mid][0]:
            print([mid,0])
            break
        elif A[mid][0] < x:
            l = mid + 1
            while l1<=r1 :
                mid2 = l1 + (r1 - l1) // 2
                if A[mid][mid2]==x:
                    print([mid,mid2])
                    break
                elif A[mid][mid2]<x:
                    l1=mid2+1
                else:
                    r1=mid2-1
            if A[mid][mid2]==x:
                break
        else:
            r = mid - 1