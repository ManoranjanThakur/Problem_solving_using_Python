def search(arr,ele):
    start=0
    end=len(arr)-1
    while(end>=0 and start>=0 and start<len(arr)-1):
        if arr[start][end]==ele:
            return [start,end]
        elif arr[start][end]>ele:
            end-=1
        elif arr[start][end]<ele:
            start+=1
    return -1


arr=[[10,20,30,40],[15,25,35,45],[17,29,37,48],[32,33,39,50]]
print(search(arr,45))