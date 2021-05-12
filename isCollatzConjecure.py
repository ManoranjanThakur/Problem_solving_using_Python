n=int(input())
A=[]
while(True):
    if n==1:
        print("Yes")
        break
    if n in A:
        print("NO")
        break
    else:
        A.append(n)
    if(n%2==0):
        n//=2
    else:
        n=3*n+1