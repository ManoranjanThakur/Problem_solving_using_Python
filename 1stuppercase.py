A='Work'
def recurf(A):
    if len(A)==0:
        return ""
    if A[0].isupper() :
        return A[0]
    return recurf(A[1:])





print(recurf(A))
B='work'
print(recurf(B))
