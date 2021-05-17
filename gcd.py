a=98
b=56

def recur(a,b,n=1):
    if n>a or n>b:
        return 0
    A=[0]
    if a%n==0 and b%n==0:
        A.append(n)
    A.append(recur(a,b,n+1))
    return max(A)

print(recur(a,b))