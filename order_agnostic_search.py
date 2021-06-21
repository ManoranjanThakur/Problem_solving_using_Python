def binarysearch(arr,ele):
    start=0
    end=len(arr)-1
    if arr[start]<arr[end]:
        while(start<=end):
            mid=start+(end-start//2)
            if arr[mid]==ele:
                return mid
            elif arr[mid]<ele:
                start=mid+1
            else:
                end=mid-1
    else:
        while(start<=end):
            mid=start+(end-start//2)
            if arr[mid]==ele:
                return mid
            elif arr[mid]<ele:
                end=mid-1
            else:
                start=mid+1
arr=[1,2,3,4,5,6,7,8]
arr2=[9,8,7,6,5,4,3,2,1]
ele=6
print("index of",ele,"is",binarysearch(arr,ele))
print("index of",ele,"is",binarysearch(arr2,ele))