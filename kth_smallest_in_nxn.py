A=[[1,5,9],
    [10,11,13],
    [12,13,15]]
t=[]
k=8
for i in range(len(A)):
    for j in range(len((A)[i])):
        t.append(A[i][j])
t=sorted(t)
print(t[k-1])
