def bs(arr,key):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=start+((end-start)//2)
        if arr[mid]==key:
            start=mid+1
        elif (ord(arr[mid])>ord(key)):
            res=mid
            end=mid-1
        else:
            start=mid+1
    return res

a=['a','b','c','d','e']
print(a[bs(a,'d')])