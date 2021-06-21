def binarysearch(arr,ele):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=start+(end-start//2)
        if arr[mid]==ele:
            res=mid
            start=mid+1
        elif arr[mid]>ele:
            end=mid-1
        elif arr[mid]<ele:
            start=mid+1
    return res
arr=[1,2,3,4,5,6,6,6,6,6,7,8,9]
ele=6
print("Index of last occurence of",ele,"is",binarysearch(arr,ele))