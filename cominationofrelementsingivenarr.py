A=[1,2,3,4,5]

def recur2(A,r,i):
    if i==r:
        return []
    for i in range 

def recur(A,r):
    if len(A)==r:
        return [A]
    o=[]
    o=o+recur(A[1:],r)


    return o

print(recur(A,3))