arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
last=len(arr)-1
def jumps(arr,pos,last):
    if pos==last:
        return 0
    if arr[pos]==0:
        return float('inf')
    min=float('inf')
    for i in range(pos+1,last+1):
        if i<(pos+arr[pos]+1):
            jump=jumps(arr,i,last)
            if(jump!=float('inf') and jump+1<min):
                min=jump+1
    return min

print(jumps(arr,0,last))

