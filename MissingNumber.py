def MN(arr):
    n=len(arr)
    total=((n+1)*(n+2)/2)
    sumi=sum(arr)
    return int(total-sumi)
n=int(input())
a = list(map(int,input().strip().split()))[:n]
print(MN(a))