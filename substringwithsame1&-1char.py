A='abcab'
n=len(A)

def recur(A,n=0):
    if A=="":
        return [""]
    if len(A)==1:
        return [""]
    a=[]
    a=a+(recur(A[1:]))
    a=a+(recur(A[:-1]))
    if A[0]==A[-1]:
        a=a+[A]
    a=list(set(a))
    if len(A)==n:
        return len(a)-1+len(A)
    return a

print(recur(A,n))