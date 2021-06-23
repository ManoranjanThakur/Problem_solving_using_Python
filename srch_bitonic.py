def bs(a,ele):
    start=0
    end=len(a)-1
    while(start<=end):
        mid=start+(end-start)//2
        if a[mid]==ele:
            return mid
        elif a[mid]<ele:
            start=mid+1
        else:
            end=mid-1
    return -1
def peak(arr):
    N=len(arr)
    start=0
    end=N-1
    while(start<=end):
        mid=start+(end-start)//2
        if mid+1<=N-1 and mid-1>=0:
            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                return mid
            elif arr[mid]<arr[mid+1]:
                start=mid+1
            else:
                end=mid-1
        elif mid-1<0:
            if arr[mid]>arr[mid+1]:
                return mid
        else:
            if arr[mid]>arr[mid-1]:
                return mid
arr=[3,4,5,7,8,9,10,11,12,13,11,10,9]
a=peak(arr)
print(max(bs(arr[0:a],3),bs(arr[a:],3)))