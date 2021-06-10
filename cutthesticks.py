a=[1,2,3,4,3,3,2,1]
n=len(a)
def rem(a,mini):
    if a==1 or min(a)==max(a):
        return a
    if mini in a:
        a.remove(mini)
        rem(a,mini)
    return a

while(n>1):
    if min(a)==max(a):
        break
    print(n)
    mini=min(a)
    a=rem(a,mini)
    n=len(a)
    for i in range(n):
        a[i]=a[i]-mini
print(len(a))


