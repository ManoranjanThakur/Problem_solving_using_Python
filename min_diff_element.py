def search(arr,key):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=start+(end-start)//2
        if arr[mid]==key:
            return 0
        elif arr[mid]>key:
            end=mid-1
        else:
            start=mid+1

    return abs(key-arr[end])

a=[1,2,3,6,9,10]
print(search(a,7))
