def first_occurence(arr,ele):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=start+(end-start//2)
        if arr[mid]==ele:
            res=mid
            end=mid-1
        elif arr[mid]>ele:
            end=mid-1
        else:
            start=mid+1
    return res
def last_occurence(arr,ele):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=start+(end-start//2)
        if arr[mid]==ele:
            res=mid
            start=mid+1
        elif arr[mid]>ele:
            end=mid-1
        else:
            start=mid+1
    return res

arr=[1,2,3,4,5,5,5,5,6,7,8,9]
ele=5
print("Count of",ele,"is",last_occurence(arr,ele)-first_occurence(arr,ele)+1)
