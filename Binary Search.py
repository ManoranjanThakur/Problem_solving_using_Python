def binarysearch(a,ele):
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
arr=[1,2,3,4,5,6,7,8,9]
print("Index of 5 is",binarysearch(arr,5))