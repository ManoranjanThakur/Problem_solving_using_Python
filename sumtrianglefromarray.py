A=[]
def recur(A):
    if len(A)<=1:
        if len(A)==1:
            print(A)
        return 0
    C=[]
    for i in range(len(A)-1):
        C.append(A[i]+A[i+1])
    recur(C)
    print(A)
    return 0
recur(A)