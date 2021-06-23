def isvalid(arr,key,mid):
    student=1
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if(sum>mid):
            student+=1
            sum=arr[i]
        if (student>key):
            return False
    return True
def allocate(arr,key):
    if(len(arr)<key):
        return -1
    start=max(arr)
    end=sum(arr)
    res=-1
    while(start<=end):
        mid=start+(end-start)//2
        if(isvalid(arr,key,mid)==True):
            res=mid
            end=mid-1
        else:
            start=mid+1
    return res
arr=[10,20,30,40,50]
print(allocate(arr,2))
