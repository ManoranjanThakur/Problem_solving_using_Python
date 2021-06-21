def binaryseacrh(a,ele):
    start=0
    end=len(a)-1
    while(start<=end):
        mid=start+(end-start//2)
        if a[mid]==ele:
            return mid
        elif a[mid]>mid:
            start=mid+1
        else:
            end=mid-1
arr=[6,5,4,3,2,1,0]
ele=4
print("Index of",ele,"is",binaryseacrh(arr,ele))