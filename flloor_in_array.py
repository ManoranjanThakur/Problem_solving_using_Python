def bs(arr,ele):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=start+((end-start)//2)
        if arr[mid]==ele:
            return mid
        elif arr[mid]<ele:
            res=mid
            start=mid+1
        else:
            end=mid-1
    return res

a=[1,2,3,5,6,7]
print(a[bs(a,4)])
