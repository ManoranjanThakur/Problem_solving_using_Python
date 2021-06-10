A=[1,2,[5,4],[6,7],[7,8,[9,10,[10,10]]]]
def recur(A):
    if len(A)==1:
        return 0
    total=0
    for i in A:
        if type(i)==type([]):
            total=total+recur(i)
        else:
            total=total+i
    return total

print(recur(A))