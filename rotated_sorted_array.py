def binary_search_i(arr,ele):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=start+((end-start)//2)
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele:
            end=mid-1
        else:
            start=mid+1
    return -1

def binary_search(arr):
    N=len(arr)
    start=0
    end=N-1
    while(start<=end):
        mid=start+((end-start)//2)
        next=(mid+1)%N
        prev=(mid+N-1)%N
        if arr[mid]<arr[next] and arr[mid]<arr[prev]:
            return N
        elif (arr[mid]>arr[0]):
            start=mid+1
        else:
            end=mid-1
    return 0
arr=[2,3,4,5,6,7,8,9,10,1]
a=binary_search_i(arr[0:(binary_search(arr))],9)
b=binary_search_i(arr[(binary_search(arr)):],9)
if a==-1:
    print(b)
else:
    print(a)
