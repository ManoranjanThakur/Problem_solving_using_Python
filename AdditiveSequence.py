A='199100'
def revfind(n1,n2,A1,found):
    if A1=="" and found:
        return True
    n3=int(n1)+int(n2)
    if A1[0:len(str(n3))]==str(n3):
        return revfind(n2,str(n3),A1[len(str(n3)):],True)
    return False
def isAdditive(A):
    n=len(A)
    if n==0:
        return False
    for i in range(1,n-1):
        if A[i]==" ":
            break
        n1=A[0:i]
        if str(int(n1))!=A[0:i]:
            break
        for j in range(i+1,n):
            if A[j]==" ":
                break
            n2=A[i:j]
            if str(int(n2))!=A[i:j]:
                break
            find=revfind(n1,n2,A[j:],False)
            if find:
                return True
    return False

print(isAdditive(A))
